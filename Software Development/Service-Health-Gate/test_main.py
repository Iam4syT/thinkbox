import json
import tempfile
import unittest
from pathlib import Path

from main import evaluate


class GateTests(unittest.TestCase):
    def evaluate_input(self, checks):
        with tempfile.TemporaryDirectory() as folder:
            file = Path(folder) / "sample.json"
            file.write_text(json.dumps(checks), encoding="utf-8")
            return evaluate(file)

    def test_threshold_is_inclusive(self):
        self.assertEqual(self.evaluate_input([{"status": 200, "latency_ms": 250}]), [])

    def test_status_and_latency_failures(self):
        self.assertEqual(self.evaluate_input([
            {"status": 503, "latency_ms": 20},
            {"status": 200, "latency_ms": 251},
        ]), [1, 2])

    def test_empty_input(self):
        with self.assertRaisesRegex(ValueError, "nonempty"):
            self.evaluate_input([])

    def test_rejects_boolean_latency(self):
        with self.assertRaisesRegex(ValueError, "invalid"):
            self.evaluate_input([{"status": 200, "latency_ms": False}])


if __name__ == "__main__":
    unittest.main()
