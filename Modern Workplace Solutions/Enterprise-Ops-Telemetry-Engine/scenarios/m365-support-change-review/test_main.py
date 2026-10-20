import unittest,copy,json
from main import analyse
from pathlib import Path
class Checks(unittest.TestCase):
 def setUp(self): self.data=json.loads(Path("fixtures.json").read_text())
 def test_unknown_negative_holds(self): self.assertEqual(analyse(self.data)["change_status"],"hold")
 def test_all_pass_needs_human(self):
  self.data["change"]["negative_test"]="pass"; r=analyse(self.data); self.assertEqual(r["change_status"],"ready_for_human_review"); self.assertFalse(r["deployment_authorised"])
 def test_failed_rollback(self): self.data["change"]["rollback_test"]="fail"; self.assertIn("rollback_test",analyse(self.data)["unresolved"])
 def test_recurring_group(self): self.assertEqual(analyse(self.data)["recurring"],[dict(service="Copilot",symptom="missing_app",count=2)])
 def test_no_duplicate_inflation(self): self.data["tickets"].append(self.data["tickets"][0]); self.assertRaises(ValueError,analyse,self.data)
 def test_bad_service(self): self.data["tickets"][0]["service"]="Unknown"; self.assertRaises(ValueError,analyse,self.data)
 def test_bad_evidence(self): self.data["change"]["approved"]="yes"; self.assertRaises(ValueError,analyse,self.data)
 def test_failed_positive_holds(self): self.data["change"]["positive_test"]="fail"; self.assertEqual(analyse(self.data)["change_status"],"hold")
if __name__=="__main__":unittest.main()
