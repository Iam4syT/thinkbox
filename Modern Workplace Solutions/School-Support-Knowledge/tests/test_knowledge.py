import unittest,sys,json,copy,tempfile,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'src'))
from knowledge_check import analyse
class KnowledgeTests(unittest.TestCase):
 def setUp(self): self.data=json.loads((ROOT/'data/history.json').read_text())
 def test_repeat_and_approved_only(self):
  r=analyse(self.data,'2026-10-08');e=r['groups'][0];p=r['groups'][1]
  self.assertEqual(e['resolved_count'],2);self.assertTrue(e['recurring']);self.assertEqual(e['article_ids'],['KB1'])
  self.assertEqual(p['resolved_count'],1);self.assertEqual(p['article_ids'],[]);self.assertTrue(p['needs_review'])
 def test_sensitive_excluded(self):
  r=analyse(self.data,'2026-10-08');self.assertEqual(r['excluded_sensitive'],1);self.assertNotIn('Restricted',json.dumps(r))
 def test_expiry_boundary(self):
  self.assertEqual(analyse(self.data,'2026-10-09')['groups'][0]['article_ids'],[])
 def test_duplicate_rejected(self):
  self.data['tickets'].append(self.data['tickets'][0])
  with self.assertRaises(ValueError):analyse(self.data,'2026-10-08')
 def test_free_text_rejected(self):
  self.data['tickets'][0]['notes']='private'
  with self.assertRaises(ValueError):analyse(self.data,'2026-10-08')
 def test_invalid_approval(self):
  self.data['articles'][0]['approved']='false'
  with self.assertRaises(ValueError):analyse(self.data,'2026-10-08')
 def test_input_unchanged(self):
  old=copy.deepcopy(self.data);analyse(self.data,'2026-10-08');self.assertEqual(self.data,old)
 def test_bad_run_preserves_output(self):
  with tempfile.TemporaryDirectory() as d:
   source=Path(d)/'bad.json';out=Path(d)/'out.json';source.write_text('{}');out.write_text('previous')
   r=subprocess.run([sys.executable,str(ROOT/'src/knowledge_check.py'),str(source),str(out),'--as-of','2026-10-08'],capture_output=True)
   self.assertEqual(r.returncode,2);self.assertEqual(out.read_text(),'previous')
if __name__=='__main__':unittest.main()
