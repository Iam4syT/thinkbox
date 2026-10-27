import unittest, json, copy, importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("review",ROOT/"scripts/review.py"); mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
class Behaviour(unittest.TestCase):
 def setUp(self):self.rows=json.loads((ROOT/"fixtures/sample.json").read_text())
 def test_duplicate(self):
  self.rows.append(copy.deepcopy(self.rows[0]))
  with self.assertRaises(ValueError):mod.review(self.rows)
 def test_empty(self):
  with self.assertRaises(ValueError):mod.review([])
 def test_nonrecord(self):
  with self.assertRaises(ValueError):mod.review([None])
 def test_identity_missing(self):
  self.rows[0]["tenant"]=" "
  with self.assertRaises(ValueError):mod.review(self.rows)
 def test_source_unchanged(self):
  before=copy.deepcopy(self.rows);mod.review(self.rows);self.assertEqual(before,self.rows)
 def test_complete_still_human(self):
  out=mod.review(self.rows)[0];self.assertEqual(out["review_state"],"human_review");self.assertFalse(out["case_closed"]);self.assertFalse(out["access_granted"])
 def test_tenant_boundary(self):
  row=self.rows[0];row["evidence_tenant"]="demo-b";self.assertIn("Evidence belongs to another tenant",mod.review([row])[0]["reasons"])
 def test_authority(self):
  self.rows[0]["access_authorised"]="yes";self.assertEqual(mod.review(self.rows)[0]["review_state"],"hold")
 def test_missing_field(self):
  del self.rows[0]["checks"];self.assertIn("Missing checks",mod.review(self.rows)[0]["reasons"])
 def test_sanitisation(self):
  self.rows[0]["sanitised"]=False;self.assertIn("Sanitisation unconfirmed",mod.review(self.rows)[0]["reasons"])
 def test_owner_preserved(self):self.assertEqual(mod.review(self.rows)[1]["owner"],"demo-analyst")
