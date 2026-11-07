import copy,json,unittest
from pathlib import Path
from review import review
class TicketChecks(unittest.TestCase):
 def setUp(self):self.rows=json.loads(Path("sample.json").read_text())
 def test_boundary(self):self.assertEqual([r["id"] for r in review(self.rows,"north-demo")],["T1","T2"])
 def test_security(self):self.assertEqual(review(self.rows,"south-demo")[0]["action"],"security escalation")
 def test_handover(self):self.assertEqual(review(self.rows,"north-demo")[1]["missing"],["owner","next_update"])
 def test_unknown_tenant(self):self.assertEqual(review(self.rows,"absent"),[])
 def test_duplicate(self):
  self.rows.append(self.rows[0].copy())
  with self.assertRaises(ValueError):review(self.rows,"north-demo")
 def test_invalid_impact(self):
  self.rows[0]["impact"]=True
  with self.assertRaises(ValueError):review(self.rows,"north-demo")
 def test_string_boolean(self):
  self.rows[0]["security"]="false"
  with self.assertRaises(ValueError):review(self.rows,"north-demo")
 def test_missing_field(self):
  del self.rows[0]["service"]
  with self.assertRaises(ValueError):review(self.rows,"north-demo")
 def test_no_mutation(self):
  before=copy.deepcopy(self.rows);review(self.rows,"north-demo");self.assertEqual(before,self.rows)
 def test_human_review(self):self.assertTrue(all(x["human_review"] for x in review(self.rows,"north-demo")))
if __name__=="__main__":unittest.main()
