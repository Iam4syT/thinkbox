import unittest
from check import evaluate,RULES
class EvidenceChecks(unittest.TestCase):
 def setUp(self): self.good={key:True for key in RULES}
 def test_complete(self): self.assertEqual(evaluate(self.good)["status"],"CHECKS_PASS")
 def test_failed_each_check(self):
  for key in RULES:
   with self.subTest(key=key):
    bad=dict(self.good);bad[key]=False
    self.assertEqual(evaluate(bad)["status"],"HOLD");self.assertIn(key,evaluate(bad)["failed"])
 def test_missing_is_not_pass(self):
  for key in RULES:
   bad=dict(self.good);del bad[key];self.assertEqual(evaluate(bad)["status"],"REVIEW")
 def test_string_true_rejected(self):
  bad=dict(self.good);bad[RULES[0]]="true"
  with self.assertRaises(ValueError): evaluate(bad)
 def test_null_rejected(self):
  bad=dict(self.good);bad[RULES[0]]=None
  with self.assertRaises(ValueError): evaluate(bad)
 def test_wrong_shape(self):
  with self.assertRaises(ValueError): evaluate([])
if __name__=="__main__":unittest.main()
