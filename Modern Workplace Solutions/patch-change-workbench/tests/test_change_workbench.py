import copy
import json
from pathlib import Path
import sys
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
from change_workbench import plan
ROOT=Path(__file__).resolve().parents[1]

class ChangeTests(unittest.TestCase):
    def setUp(self): self.payload=json.loads((ROOT/"templates/findings.json").read_text())
    def rows(self): return {r["id"]:r for r in plan(self.payload)["results"]}
    def test_six_distinct_workflow_states(self):
        self.assertEqual([self.rows()["LAB-VULN-0"+str(i)]["state"] for i in range(1,7)],["needs_approval","ready_for_pilot","risk_escalation","verify_again","closed_verified_in_fixture","rollback_review"])
    def test_external_critical_first(self): self.assertEqual(plan(self.payload)["results"][0]["id"],"LAB-VULN-03")
    def test_no_approval_cannot_close(self):
        self.payload["findings"][4]["approved"]=False
        self.assertEqual(self.rows()["LAB-VULN-05"]["state"],"needs_approval")
    def test_old_version_cannot_close(self):
        self.payload["findings"][4]["observed_version"]="1.9.99"
        self.assertEqual(self.rows()["LAB-VULN-05"]["state"],"verify_again")
    def test_recheck_unknown_cannot_close(self):
        self.payload["findings"][4]["security_recheck_pass"]=None
        self.assertEqual(self.rows()["LAB-VULN-05"]["state"],"verify_again")
    def test_unknown_exposure_escalates(self):
        self.payload["findings"][1]["exposure"]="unknown"
        self.assertEqual(self.rows()["LAB-VULN-02"]["state"],"risk_escalation")
    def test_string_approval_rejected(self):
        self.payload["findings"][1]["approved"]="false"
        with self.assertRaises(ValueError): plan(self.payload)
    def test_duplicate_rejected(self):
        self.payload["findings"].append(copy.deepcopy(self.payload["findings"][0]))
        with self.assertRaises(ValueError): plan(self.payload)
    def test_empty_is_not_success(self):
        result=plan({"findings":[]})
        self.assertTrue(result["no_data"])
        self.assertFalse(result["live_remediation_established"])
    def test_semantic_numeric_version(self):
        item=self.payload["findings"][4]
        item["target_version"]="2.9"
        item["observed_version"]="2.10"
        self.assertEqual(self.rows()["LAB-VULN-05"]["state"],"closed_verified_in_fixture")

if __name__ == "__main__": unittest.main()
