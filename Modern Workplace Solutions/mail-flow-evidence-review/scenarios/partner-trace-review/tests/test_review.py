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
 def test_each_status(self):
  out=mod.review(self.rows);self.assertEqual([x["status"] for x in out],["Delivered","Failed","Deferred","Unknown"]);self.assertTrue(all(x["human_review_required"] and not x["setting_changed"] for x in out))
 def test_no_authority(self):
  self.rows[0]["access_authorised"]=False;self.assertTrue(mod.review(self.rows)[0]["next_action"].startswith("Stop"))
 def test_authority_not_truthy(self):
  self.rows[0]["access_authorised"]="yes";self.assertTrue(mod.review(self.rows)[0]["next_action"].startswith("Stop"))
 def test_delivered_not_closed(self):self.assertIn("not proof",mod.review(self.rows)[0]["next_action"])
 def test_bad_status(self):
  self.rows[0]["trace_status"]="Closed"
  with self.assertRaises(ValueError):mod.review(self.rows)
