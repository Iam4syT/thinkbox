import sys,json,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from pilot import check,detect
P=Path(__file__).resolve().parents[1]
class PilotTests(unittest.TestCase):
 def setUp(self): self.p=json.loads((P/'templates/package.json').read_text())
 def test_valid(self): self.assertFalse(check(self.p)['native_validated'])
 def test_broad_assignment_rejected(self):
  self.p['pilot']=['ALL-DEVICES']
  with self.assertRaises(ValueError):check(self.p)
 def test_missing_uninstall_rejected(self):
  del self.p['uninstall']
  with self.assertRaises(ValueError):check(self.p)
 def test_duplicate_target_rejected(self):
  self.p['pilot']=['LAB-WIN01','LAB-WIN01']
  with self.assertRaises(ValueError):check(self.p)
 def test_bad_architecture_rejected(self):
  self.p['architecture']='unknown'
  with self.assertRaises(ValueError):check(self.p)
 def test_wrong_version_not_detected(self): self.assertFalse(detect('1.0.0','0.9.0'))
 def test_absent_not_detected(self): self.assertFalse(detect('1.0.0',None))
if __name__=='__main__':unittest.main()
