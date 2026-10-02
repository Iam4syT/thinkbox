import unittest
from readiness import assess
class ReadinessTests(unittest.TestCase):
 def setUp(self):self.good={'id':'a','approval':True,'action':'join','licence':'test','mfa_registered':True,'asset_id':'x','mdm_state':'managed','groups':['staff']}
 def test_ready_is_review_not_execute(self):self.assertEqual(assess([self.good])[0]['status'],'ready-for-human-review')
 def test_missing_approval(self):self.assertIn('approval-missing',assess([{**self.good,'approval':False}])[0]['issues'])
 def test_privileged_group(self):self.assertIn('unexpected-group',assess([{**self.good,'groups':['global-admin']}])[0]['issues'])
 def test_unmanaged(self):self.assertIn('mdm-not-confirmed',assess([{**self.good,'mdm_state':'unknown'}])[0]['issues'])
 def test_duplicate(self):self.assertIn('missing-or-duplicate-id',assess([self.good,self.good])[1]['issues'])
 def test_leaver_retention(self):self.assertIn('retention-review-missing',assess([{'id':'l','action':'leave','approval':True,'asset_returned':True}])[0]['issues'])
 def test_empty(self):self.assertEqual(assess([]),[])
if __name__=='__main__':unittest.main()
