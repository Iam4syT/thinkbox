import tempfile
import unittest
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from Analytics.LogParser import generate_mock_telemetry
from Analytics.anomalous_noise_detector import detect_systemic_anomalies

class TelemetryTests(unittest.TestCase):
    def test_repeatable_baseline_and_holdout(self):
        with tempfile.TemporaryDirectory() as temp:
            a = generate_mock_telemetry(200, output_dir=temp)
            b = generate_mock_telemetry(200, output_dir=temp)
            self.assertTrue(a.equals(b))
            result = detect_systemic_anomalies(Path(temp)/"azure_telemetry_raw.csv", temp)
            self.assertEqual(result["train_size"] + result["test_size"], 200)
            self.assertEqual(result["threshold_baseline"]["false_negative"], 0)
            self.assertEqual(result["threshold_baseline"]["false_positive"], 0)
    def test_invalid_small_fixture(self):
        with self.assertRaises(ValueError): generate_mock_telemetry(1)
