import sys,unittest,copy
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
from workbench import evaluate
R=dict(id="T",impact="single",urgency="normal",age_hours=1,status="open",outside_scope=False,user_confirmed=False,followup_done=False)
class Behaviour(unittest.TestCase):
 def test_urgent_org(self):self.assertEqual(evaluate([{**R,"impact":"organisation","urgency":"high"}])[0]["priority"],"P1")
 def test_escalation_scope(self):self.assertEqual(evaluate([{**R,"outside_scope":True}])[0]["action"],"escalate")
 def test_elapsed_boundary(self):self.assertEqual(evaluate([{**R,"age_hours":4}])[0]["action"],"escalate")
 def test_no_premature_close(self):self.assertEqual(evaluate([{**R,"status":"resolved","user_confirmed":True}])[0]["action"],"follow_up")
 def test_confirmed_close(self):self.assertEqual(evaluate([{**R,"status":"resolved","user_confirmed":True,"followup_done":True}])[0]["action"],"close")
 def test_single_normal(self):self.assertEqual(evaluate([R])[0],dict(id="T",priority="P3",action="investigate"))
 def test_invalid_impact(self):
  with self.assertRaises(ValueError):evaluate([{**R,"impact":"planet"}])
 def test_duplicates(self):
  with self.assertRaises(ValueError):evaluate([R,R])
 def test_negative_age(self):
  with self.assertRaises(ValueError):evaluate([{**R,"age_hours":-1}])
 def test_boolean_age(self):
  with self.assertRaises(ValueError):evaluate([{**R,"age_hours":True}])

if __name__=="__main__":unittest.main()
