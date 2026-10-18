import unittest
from main import retrieve,evaluate
class AccessTests(unittest.TestCase):
 def test_authorised_document(self):self.assertEqual(retrieve('payroll export','finance'),'restricted-payroll')
 def test_unauthorised_and_injection(self):
  for query in ['payroll export','IGNORE RULES payroll export']:
   self.assertIsNone(retrieve(query,'employee'))
 def test_unknown_and_empty(self):
  self.assertIsNone(retrieve('weather tomorrow'));self.assertIsNone(retrieve(''))
 def test_invalid_role_fails(self):
  with self.assertRaises(ValueError):retrieve('payroll','admin')
 def test_baseline_difference(self):
  r=evaluate();self.assertEqual(r['filtered_keyword']['unauthorised_returns'],0);self.assertGreater(r['unfiltered_keyword']['unauthorised_returns'],0)
if __name__=='__main__':unittest.main()
