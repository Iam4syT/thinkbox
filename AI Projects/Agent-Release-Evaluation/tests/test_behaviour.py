import unittest,copy,json
from pathlib import Path
from main import evaluate,batch
class Gate(unittest.TestCase):
 def setUp(self): self.row=json.loads(Path("data/traces.json").read_text())[0]
 def bad(self,**changes): return {**self.row,**changes}
 def test_normal_needs_review(self): self.assertEqual(evaluate(self.row)["status"],"READY_FOR_REVIEW")
 def test_tool(self): self.assertIn("tool_allowlist",evaluate(self.bad(tools=["send_email"]))["failed"])
 def test_citation(self): self.assertIn("citation_scope",evaluate(self.bad(citations=["B"]))["failed"])
 def test_empty_citation(self): self.assertIn("citation_scope",evaluate(self.bad(citations=[]))["failed"])
 def test_review(self): self.assertIn("human_review",evaluate(self.bad(human_review=False))["failed"])
 def test_string_review(self): self.assertRaises(ValueError,evaluate,self.bad(human_review="true"))
 def test_boolean_tokens(self): self.assertRaises(ValueError,evaluate,self.bad(tokens_in=True))
 def test_negative(self): self.assertRaises(ValueError,evaluate,self.bad(tokens_out=-1))
 def test_nan(self): self.assertRaises(ValueError,evaluate,self.bad(quality=float("nan")))
 def test_budgets(self): self.assertEqual(set(evaluate(self.bad(tokens_out=900,latency_ms=2001,quality=.79))["failed"]),{"token_budget","latency_budget","quality"})
 def test_unknown_field(self): self.assertRaises(ValueError,evaluate,self.bad(secret="bad"))
 def test_duplicate(self): self.assertRaises(ValueError,batch,[self.row,self.row])
 def test_boundaries(self): self.assertEqual(evaluate(self.bad(tokens_in=500,tokens_out=500,latency_ms=2000,quality=.8))["status"],"READY_FOR_REVIEW")
 def test_cost_arithmetic(self): self.assertAlmostEqual(evaluate(self.row)["illustrative_cost_units"],.0007)
