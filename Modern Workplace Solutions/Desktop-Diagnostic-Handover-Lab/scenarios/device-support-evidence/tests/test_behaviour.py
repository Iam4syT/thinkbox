import importlib.util, json, unittest, tempfile, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("checker",ROOT/"scripts/check.py")
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
class Behaviour(unittest.TestCase):
 def sample(self): return json.loads((ROOT/"templates/sample.json").read_text())
 def test_manual_states(self):
  self.assertEqual([x['state'] for x in m.evaluate(self.sample())], ['review_failure', 'collect_evidence', 'ready_for_human_closure', 'review_failure'])
 def test_unknown_retained(self):
  r={"id":"X",**{f:None for f in m.FIELDS}}
  self.assertEqual(set(m.evaluate([r])[0]['missing']),set(m.FIELDS))
 def test_bad_type(self):
  r=self.sample(); r[0][m.FIELDS[0]]='false'
  with self.assertRaises(ValueError): m.evaluate(r)
 def test_duplicate(self):
  r=self.sample()
  with self.assertRaises(ValueError): m.evaluate([r[0],r[0]])
 def test_empty_or_extra_rejected(self):
  for r in [[],{},[{'id':'X','extra':True}]]:
   with self.assertRaises(ValueError): m.evaluate(r)
 def test_failure_and_unknown_coexist(self):
  r={"id":"X",**{f:None for f in m.FIELDS}}; r[m.FIELDS[0]]=False
  x=m.evaluate([r])[0]; self.assertIn(m.FIELDS[0],x['failed']); self.assertIn(m.FIELDS[1],x['missing'])
 def test_invalid_input_preserves_output(self):
  with tempfile.TemporaryDirectory() as d:
   src=Path(d)/'in.json'; out=Path(d)/'out.json'
   src.write_text('{}'); out.write_text('previous')
   r=subprocess.run([sys.executable,str(ROOT/'scripts/check.py'),str(src),str(out)],capture_output=True)
   self.assertNotEqual(r.returncode,0); self.assertEqual(out.read_text(),'previous')
 def test_no_automatic_change(self):
  for x in m.evaluate(self.sample()): self.assertFalse(x.get('closed',False)); self.assertFalse(x.get('changed',False)); self.assertFalse(x.get('root_cause_confirmed',False))
 def test_same_path_rejected(self):
  with tempfile.TemporaryDirectory() as d:
   src=Path(d)/'in.json'; src.write_text(json.dumps(self.sample())); before=src.read_bytes()
   r=subprocess.run([sys.executable,str(ROOT/'scripts/check.py'),str(src),str(src)],capture_output=True)
   self.assertNotEqual(r.returncode,0); self.assertEqual(src.read_bytes(),before)
if __name__=='__main__': unittest.main()
