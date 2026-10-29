import unittest,sys,json,copy,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from check import review,CHECKS,IDENTIFIER
class Checks(unittest.TestCase):
 def setUp(self): self.d=json.loads((ROOT/'templates/sample.json').read_text())
 def test_normal(self): self.assertEqual(review(self.d)['status'],'ready_for_human_review')
 def test_failed_path(self): self.d['checks'][CHECKS[-1]]='fail'; self.assertEqual(review(self.d)['status'],'hold')
 def test_unknown_path(self): self.d['checks'][CHECKS[0]]='unknown'; self.assertEqual(review(self.d)['status'],'review')
 def test_failure_overrides_unknown(self): self.d['checks'][CHECKS[0]]='unknown';self.d['checks'][CHECKS[-1]]='fail';self.assertEqual(review(self.d)['status'],'hold')
 def test_missing_owner(self): del self.d['owner'];self.assertRaises(ValueError,review,self.d)
 def test_blank_id(self): self.d[IDENTIFIER]='  ';self.assertRaises(ValueError,review,self.d)
 def test_missing_check(self): del self.d['checks'][CHECKS[0]];self.assertRaises(ValueError,review,self.d)
 def test_extra_check(self): self.d['checks']['surprise']='pass';self.assertRaises(ValueError,review,self.d)
 def test_bool_not_observation(self): self.d['checks'][CHECKS[0]]=True;self.assertRaises(ValueError,review,self.d)
 def test_unknown_word(self): self.d['checks'][CHECKS[0]]='yes';self.assertRaises(ValueError,review,self.d)
 def test_input_unchanged(self): original=copy.deepcopy(self.d);review(self.d);self.assertEqual(self.d,original)
 def test_cli_bad_file(self): r=subprocess.run([sys.executable,str(ROOT/'scripts/check.py'),'does-not-exist.json'],capture_output=True,text=True);self.assertEqual(r.returncode,2);self.assertIn('Input error',r.stderr)
if __name__=='__main__':unittest.main()
