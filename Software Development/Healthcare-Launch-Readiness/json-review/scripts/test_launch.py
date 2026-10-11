import unittest
from check_launch import check,REQUIRED
class Tests(unittest.TestCase):
 def data(self):return {"launch_id":"L1","checks":{k:{"status":"passed","evidence":"demo-note"} for k in REQUIRED}}
 def test_complete_review_only(self):self.assertEqual(check(self.data())["decision"],"ready-for-human-review")
 def test_missing_reference_holds(self):
  d=self.data();d["checks"]["rollback"]["evidence"]="";self.assertEqual(check(d)["missing_or_failed"],["rollback"])
 def test_failed_holds(self):
  d=self.data();d["checks"]["training"]["status"]="failed";self.assertEqual(check(d)["decision"],"hold")
 def test_pending_holds(self):
  d=self.data();d["checks"]["support_owner"]["status"]="pending";self.assertEqual(check(d)["decision"],"hold")
 def test_missing_check_rejected(self):
  d=self.data();del d["checks"]["training"]
  with self.assertRaises(ValueError):check(d)
 def test_unknown_status_rejected(self):
  d=self.data();d["checks"]["training"]["status"]="done"
  with self.assertRaises(ValueError):check(d)
 def test_blank_id_rejected(self):
  d=self.data();d["launch_id"]=" "
  with self.assertRaises(ValueError):check(d)
 def test_input_shape_rejected(self):
  with self.assertRaises(ValueError):check([])
