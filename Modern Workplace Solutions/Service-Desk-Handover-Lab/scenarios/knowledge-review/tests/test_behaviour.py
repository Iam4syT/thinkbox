import sys,unittest,copy
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
from workbench import evaluate
R=dict(id="K",owner="reviewer",symptom="demo error",safe_steps="check status",verification="retry",escalation="demo team",reviewed=True,review_due="2026-10-29")
def run(r):return evaluate([r],"2026-10-29")[0]
class Behaviour(unittest.TestCase):
 def test_ready(self):self.assertEqual(run(R)["status"],"ready")
 def test_missing_verification(self):self.assertIn("verification",run({**R,"verification":""})["reasons"])
 def test_no_approval(self):self.assertIn("approval",run({**R,"reviewed":False})["reasons"])
 def test_overdue(self):self.assertIn("overdue",run({**R,"review_due":"2026-10-28"})["reasons"])
 def test_due_today(self):self.assertEqual(run(R)["status"],"ready")
 def test_missing_owner(self):self.assertIn("owner",run({**R,"owner":" "})["reasons"])
 def test_duplicates(self):
  with self.assertRaises(ValueError):evaluate([R,R],"2026-10-29")
 def test_bad_date(self):
  with self.assertRaises(ValueError):run({**R,"review_due":"yesterday"})
 def test_bad_review_type(self):
  with self.assertRaises(ValueError):run({**R,"reviewed":"yes"})
 def test_invalid_shape(self):
  with self.assertRaises(ValueError):evaluate({},"2026-10-29")

if __name__=="__main__":unittest.main()
