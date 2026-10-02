import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("sharepoint_review", ROOT / "scripts/review.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class ManifestTests(unittest.TestCase):
    def setUp(self):
        self.source = json.loads((ROOT / "templates/source.json").read_text())
        self.destination = json.loads((ROOT / "templates/destination.json").read_text())

    def report(self):
        return module.evaluate(self.source, self.destination)

    def codes(self):
        return {x["code"] for x in self.report()["findings"]}

    def test_complete_matching(self):
        self.assertEqual("MANIFESTS_MATCH", self.report()["state"])

    def test_missing_owner(self):
        self.source["site"]["owner"] = None
        self.assertIn("MISSING_OWNER", self.codes())

    def test_geo_unknown_not_certified(self):
        self.source["site"]["geo_verified"] = False
        self.assertIn("GEO_UNVERIFIED", self.codes())

    def test_geo_change_needs_review(self):
        self.destination["site"]["geo"] = "EUR"
        self.assertIn("GEO_DIFFERENCE", self.codes())

    def test_missing_content(self):
        self.destination["files"].pop()
        self.assertIn("MISSING_CONTENT", self.codes())

    def test_unexpected_content(self):
        f = copy.deepcopy(self.destination["files"][0]); f["path"] = "Documents/Extra.txt"
        self.destination["files"].append(f)
        self.assertIn("UNEXPECTED_CONTENT", self.codes())

    def test_content_hash_mismatch(self):
        self.destination["files"][0]["sha256"] = "0" * 64
        self.assertIn("CONTENT_MISMATCH", self.codes())

    def test_same_hash_different_size(self):
        self.destination["files"][0]["size_bytes"] += 1
        self.assertIn("CONTENT_MISMATCH", self.codes())

    def test_effective_group_declarations_change(self):
        self.destination["files"][0]["principals"] = ["Lab-Readers"]
        self.assertIn("PERMISSION_DIFFERENCE", self.codes())

    def test_metadata_loss(self):
        self.destination["files"][0]["metadata"] = {}
        self.assertIn("METADATA_DIFFERENCE", self.codes())

    def test_broad_link_and_unique_scope(self):
        self.source["files"][0].update(principals=["Anyone"], unique_permissions=True)
        self.assertTrue({"PUBLIC_LINK_REVIEW", "UNIQUE_PERMISSION_REVIEW"} <= self.codes())

    def test_empty_inventory_not_success(self):
        self.source["files"] = []; self.destination["files"] = []
        self.assertIn("EMPTY_INVENTORY", self.codes())

    def test_bad_hash_not_success(self):
        self.source["files"][0]["sha256"] = "unknown"
        with self.assertRaises(ValueError): self.report()

    def test_duplicate_path_rejected(self):
        self.source["files"].append(copy.deepcopy(self.source["files"][0]))
        with self.assertRaises(ValueError): self.report()

    def test_path_traversal_rejected(self):
        self.source["files"][0]["path"] = "../Private.txt"
        with self.assertRaises(ValueError): self.report()

    def test_deterministic_read_only(self):
        before = copy.deepcopy(self.source)
        self.assertEqual(self.report(), self.report())
        self.assertEqual(before, self.source)


if __name__ == "__main__": unittest.main()
