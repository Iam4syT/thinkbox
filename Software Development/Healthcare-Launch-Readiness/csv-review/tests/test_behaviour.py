import unittest,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
from main import review,REQUIRED
def rows():return [dict(check=n,status="pass",evidence="synthetic check",owner="reviewer",rollback="restore prior version") for n in sorted(REQUIRED)]
class Behaviour(unittest.TestCase):
    def test_complete_checks_require_human_review(self):self.assertEqual(review(rows())["decision"],"READY FOR HUMAN REVIEW")
    def test_unrun_is_hold(self):
        r=rows();r[0]["status"]="unrun";self.assertEqual(review(r)["decision"],"HOLD")
    def test_missing_evidence_is_hold(self):
        r=rows();r[0]["evidence"]="";self.assertEqual(review(r)["decision"],"HOLD")
    def test_missing_required_row_is_hold(self):self.assertIn("missing check"," ".join(review(rows()[:-1])["blockers"]))
    def test_missing_rollback_is_hold(self):
        r=rows();r[0]["rollback"]="";self.assertEqual(review(r)["decision"],"HOLD")
    def test_missing_owner_is_hold(self):
        r=rows();r[0]["owner"]="";self.assertEqual(review(r)["decision"],"HOLD")
    def test_duplicate_check_is_error(self):
        r=rows()
        with self.assertRaises(ValueError):review(r+[r[0]])
    def test_never_deploys(self):self.assertFalse(review(rows())["deployment_performed"])
