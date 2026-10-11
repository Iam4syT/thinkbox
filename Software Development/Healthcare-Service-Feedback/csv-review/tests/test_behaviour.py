import unittest,sys,tempfile
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
from main import review,load,FIELDS
def case(**kwargs):
    d=dict(id="S1",category="access",impact="single",evidence="synthetic check",owner="analyst",status="open");d.update(kwargs);return d
class Behaviour(unittest.TestCase):
    def test_safety_always_escalates(self): self.assertIn("escalate immediately",review([case(impact="safety")])["cases"][0]["review"][0])
    def test_missing_evidence_requires_action(self): self.assertIn("request reproduction evidence",review([case(evidence="")])["cases"][0]["review"])
    def test_unsupported_closure(self): self.assertIn("closure unsupported",review([case(status="closed",evidence="")])["cases"][0]["review"])
    def test_missing_owner(self): self.assertIn("assign a responsible reviewer",review([case(owner="")])["cases"][0]["review"])
    def test_duplicate_id_rejected(self):
        with self.assertRaises(ValueError): review([case(),case()])
    def test_unknown_category_rejected(self):
        with self.assertRaises(ValueError): review([case(category="unknown")])
    def test_counts_and_no_automatic_fix(self):
        r=review([case(),case(id="S2",category="report")]);self.assertEqual(r["category_counts"],{"access":1,"report":1});self.assertFalse(r["automatic_resolution"])
    def test_invalid_csv_fails_before_report(self):
        with tempfile.TemporaryDirectory() as t:
            p=Path(t)/"bad.csv";p.write_text("wrong\na\n")
            with self.assertRaises(ValueError):load(p,FIELDS)
