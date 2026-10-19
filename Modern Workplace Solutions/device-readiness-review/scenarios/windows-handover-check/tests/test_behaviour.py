import importlib.util,unittest,csv
from pathlib import Path
spec=importlib.util.spec_from_file_location("check",Path(__file__).parents[1]/"scripts/check.py");m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
class Behaviour(unittest.TestCase):
    def setUp(self):
        with (Path(__file__).parents[1]/"templates/sample.csv").open(newline="") as f:self.rows=list(csv.DictReader(f))
    def test_expected(self):
        result=m.evaluate(self.rows)
        self.assertEqual([r["missing"] for r in result],[[],["approved"],["encrypted","patched"],["m365_test","owner_recorded"]])
    def test_duplicate_rejected(self):
        with self.assertRaises(ValueError):m.evaluate(self.rows+[self.rows[0]])
    def test_bad_schema_rejected(self):
        row=dict(self.rows[0]);row["unexpected"]="x"
        with self.assertRaises(ValueError):m.evaluate([row])
    def test_bad_value_rejected(self):
        row=dict(self.rows[0]);row["encrypted"]="TRUE"
        with self.assertRaises(ValueError):m.evaluate([row])
    def test_boundary_or_unknown(self):
        row=dict(self.rows[0]);row["encrypted"]="unknown";self.assertEqual(m.evaluate([row])[0]["status"],"REVIEW")
if __name__=="__main__":unittest.main()
