import unittest, sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
from check import check, FIELDS
class Checks(unittest.TestCase):
 def fixture(self):return {k:("LAB-001" if k=="request_id" else True) for k in FIELDS}
 def test_normal(self):self.assertEqual(check(self.fixture()),"READY FOR HUMAN REVIEW")
 def test_each_missing_check_blocks(self):
  for k in FIELDS-{"request_id"}:
   with self.subTest(k=k):
    r=self.fixture();r[k]=False;self.assertIn(k,check(r));self.assertTrue(check(r).startswith("BLOCKED"))
 def test_absent(self):
  r=self.fixture();r.pop("mail")
  with self.assertRaises(ValueError):check(r)
 def test_string_bool(self):
  r=self.fixture();r["approval"]="true"
  with self.assertRaises(ValueError):check(r)
 def test_numeric_bool(self):
  r=self.fixture();r["approval"]=1
  with self.assertRaises(ValueError):check(r)
 def test_unexpected(self):
  r=self.fixture();r["email"]="private"
  with self.assertRaises(ValueError):check(r)
 def test_empty_id(self):
  r=self.fixture();r["request_id"]=" "
  with self.assertRaises(ValueError):check(r)
 def test_not_object(self):
  with self.assertRaises(ValueError):check([])
if __name__=="__main__":unittest.main()
