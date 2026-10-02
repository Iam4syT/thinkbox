import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("service_review", ROOT / "scripts/review.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
NOW = "2026-09-30T09:00:00Z"


class ReviewTests(unittest.TestCase):
    def setUp(self):
        self.good = json.loads((ROOT / "templates/healthy.json").read_text())

    def run_report(self, data=None):
        return module.evaluate(self.good if data is None else data, NOW)

    def codes(self, data=None):
        return {x["code"] for x in self.run_report(data)["findings"]}

    def test_complete_no_findings(self):
        self.assertEqual("NO_RULE_FINDINGS", self.run_report()["state"])

    def test_outage_does_not_imply_local_root_cause(self):
        self.good["services"][0]["status"] = "ServiceInterruption"
        self.assertEqual("REVIEW", self.run_report()["state"])
        self.assertIn("SERVICE_REVIEW", self.codes())

    def test_missing_workload_is_incomplete(self):
        self.good["services"].pop()
        self.assertEqual("INCOMPLETE", self.run_report()["state"])

    def test_unknown_provider_status_is_incomplete(self):
        self.good["services"][0]["status"] = "provider-new-status"
        self.assertIn("UNKNOWN_STATUS", self.codes())

    def test_stale_is_not_clean(self):
        self.good["captured_at"] = "2026-09-20T08:00:00Z"
        self.assertIn("STALE_SNAPSHOT", self.codes())

    def test_future_capture_rejected(self):
        self.good["captured_at"] = "2026-10-01T08:00:00Z"
        with self.assertRaises(ValueError): self.run_report()

    def test_zero_adoption_denominator_unknown(self):
        self.good["usage"][0].update(active_users=0, licensed_users=0)
        self.assertIn("UNKNOWN_ADOPTION", self.codes())

    def test_adoption_boundary(self):
        self.good["usage"][0]["active_users"] = 20
        self.assertNotIn("ADOPTION_REVIEW", self.codes())
        self.good["usage"][0]["active_users"] = 19
        self.assertIn("ADOPTION_REVIEW", self.codes())

    def test_capacity_boundary(self):
        self.good["storage"][0]["used_bytes"] = 90
        self.assertIn("CAPACITY_REVIEW", self.codes())

    def test_unknown_audit_collection(self):
        self.good["audit_complete"] = False
        self.good["audit_events"] = []
        self.assertEqual("INCOMPLETE", self.run_report()["state"])

    def test_invalid_number_rejected(self):
        for n in [-1, True, float("nan")]:
            data = copy.deepcopy(self.good)
            data["storage"][0]["used_bytes"] = n
            with self.assertRaises(ValueError): self.run_report(data)

    def test_duplicate_service_rejected(self):
        self.good["services"].append(copy.deepcopy(self.good["services"][0]))
        with self.assertRaises(ValueError): self.run_report()

    def test_impossible_usage_rejected(self):
        self.good["usage"][0]["active_users"] = 101
        with self.assertRaises(ValueError): self.run_report()

    def test_deterministic_read_only(self):
        before = copy.deepcopy(self.good)
        self.assertEqual(self.run_report(), self.run_report())
        self.assertEqual(before, self.good)


if __name__ == "__main__": unittest.main()
