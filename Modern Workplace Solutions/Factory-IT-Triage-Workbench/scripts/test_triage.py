import unittest
from triage import classify
class TriageTests(unittest.TestCase):
 def setUp(self):self.good={'id':'a','site':'test','asset_id':'x','symptom':'test','impact':'one user','started':'today','checks':['read only'],'zone':'office','asset_type':'windows','symptom_type':'account'}
 def test_plain(self):self.assertEqual(classify(self.good)['route'],'service-desk')
 def test_machine_boundary(self):self.assertIn('no-reboot',classify({**self.good,'asset_type':'machine-pc'})['boundary'])
 def test_stop_urgent(self):self.assertEqual(classify({**self.good,'zone':'production','production_stopped':True})['priority'],'urgent')
 def test_security_overrides(self):
  result=classify({**self.good,'zone':'production','security_suspected':True})
  self.assertEqual(result['route'],'security-and-service-manager')
  self.assertIn('no-reboot',result['boundary'])
 def test_apple_escalation(self):self.assertEqual(classify({**self.good,'asset_type':'ipad'})['route'],'mdm-specialist')
 def test_incomplete(self):self.assertEqual(classify({})['priority'],'review')
 def test_unknown(self):self.assertEqual(classify({**self.good,'symptom_type':'other'})['route'],'clarify-with-service-manager')
if __name__=='__main__':unittest.main()
