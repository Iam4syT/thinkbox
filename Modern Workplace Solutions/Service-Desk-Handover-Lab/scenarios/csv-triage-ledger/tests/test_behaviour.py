import importlib.util,unittest,csv
from pathlib import Path
spec=importlib.util.spec_from_file_location("check",Path(__file__).parents[1]/"scripts/check.py");m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
class Behaviour(unittest.TestCase):
    def setUp(self):
        with (Path(__file__).parents[1]/"templates/sample.csv").open(newline="") as f:self.rows=list(csv.DictReader(f))
    def test_expected(self):
        result=m.evaluate(self.rows)
        self.assertEqual([(r["priority"],r["route"],r["review_due"]) for r in result],[("P1","M365 support",True),("P2","Access team",False),("P3","Device team",True),("P3","Human triage",False)])
    def test_duplicate_rejected(self):
        with self.assertRaises(ValueError):m.evaluate(self.rows+[self.rows[0]])
    def test_bad_schema_rejected(self):
        row=dict(self.rows[0]);row["unexpected"]="x"
        with self.assertRaises(ValueError):m.evaluate([row])
    def test_bad_value_rejected(self):
        row=dict(self.rows[0]);row["age_minutes"]="-1"
        with self.assertRaises(ValueError):m.evaluate([row])
    def test_boundary_or_unknown(self):
        row=dict(self.rows[0]);row["age_minutes"]="14";self.assertFalse(m.evaluate([row])[0]["review_due"])
if __name__=="__main__":unittest.main()
