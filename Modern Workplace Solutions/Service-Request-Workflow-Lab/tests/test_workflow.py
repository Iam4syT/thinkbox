import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
from workflow import Workflow
class Tests(unittest.TestCase):
 def setUp(self):self.w=Workflow();self.w.add("SYN-1","a","Test")
 def test_normal_lifecycle(self):
  for v,s in enumerate(["Triaged","In progress","Resolved"],1):self.w.move("SYN-1",s,"a",v)
  self.assertEqual(self.w.snapshot()["SYN-1"]["status"],"Resolved")
 def test_duplicate(self):
  with self.assertRaises(ValueError):self.w.add("SYN-1","a","Test")
 def test_missing_owner(self):
  with self.assertRaises(ValueError):self.w.add("SYN-2","","Test")
 def test_missing_summary(self):
  with self.assertRaises(ValueError):self.w.add("SYN-2","a","")
 def test_unauthorised(self):
  with self.assertRaises(PermissionError):self.w.move("SYN-1","Triaged","b",1)
  self.assertEqual(self.w.snapshot()["SYN-1"]["version"],1)
 def test_stale_update(self):
  self.w.move("SYN-1","Triaged","a",1)
  with self.assertRaises(ValueError):self.w.move("SYN-1","In progress","a",1)
 def test_skip_triage(self):
  with self.assertRaises(ValueError):self.w.move("SYN-1","Resolved","a",1)
 def test_snapshot_is_detached(self):
  snap=self.w.snapshot();snap["SYN-1"]["owner"]="b";self.assertEqual(self.w.snapshot()["SYN-1"]["owner"],"a")
 def test_unknown_request(self):
  with self.assertRaises(KeyError):self.w.move("missing","Triaged","a",1)
if __name__=="__main__":unittest.main()
