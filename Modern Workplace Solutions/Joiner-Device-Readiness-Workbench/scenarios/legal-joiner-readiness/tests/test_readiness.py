import sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from check_readiness import assess, REQUIRED
class Readiness(unittest.TestCase):
    def test_good(self): self.assertEqual(assess(dict.fromkeys(REQUIRED,"yes"))["status"],"READY")
    def test_all_missing(self): self.assertEqual(len(assess({})["missing"]),9)
    def test_blank(self): self.assertIn("mfa",assess({**dict.fromkeys(REQUIRED,"yes"),"mfa":""})["missing"])
    def test_false(self): self.assertEqual(assess({**dict.fromkeys(REQUIRED,"yes"),"approved":"no"})["status"],"HOLD")
    def test_unknown(self): self.assertEqual(assess({**dict.fromkeys(REQUIRED,"yes"),"compliant":"unknown"})["status"],"HOLD")
    def test_case(self): self.assertEqual(assess(dict.fromkeys(REQUIRED," YES "))["status"],"READY")
    def test_missing_device(self): self.assertIn("device_enrolled",assess({**dict.fromkeys(REQUIRED,"yes"),"device_enrolled":"no"})["missing"])
    def test_no_promotion(self): self.assertEqual(assess({**dict.fromkeys(REQUIRED,"yes"),"handover":"planned"})["status"],"HOLD")
if __name__ == "__main__": unittest.main()
