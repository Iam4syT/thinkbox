import unittest,json
from pathlib import Path
from check import evaluate
class Behaviour(unittest.TestCase):
 def setUp(self):self.d=json.loads((Path(__file__).parents[1]/'templates/sample.json').read_text())
 def result(self):return evaluate(self.d)['findings'][0]['result']
 def test_normal(self):self.assertEqual(self.result(),'EVIDENCE_PASS')
 def test_expiry_boundary(self):self.d['now']='2026-10-18T13:00:00Z';self.assertEqual(self.result(),'EXPIRED')
 def test_not_started(self):self.d['now']='2026-10-18T11:00:00Z';self.assertEqual(self.result(),'NOT_STARTED')
 def test_no_approval(self):self.d['requests'][0]['approved']=False;self.assertEqual(self.result(),'DENY')
 def test_self_approval(self):self.d['requests'][0]['approver']='test-user';self.assertEqual(self.result(),'DENY')
 def test_no_mfa(self):self.d['requests'][0]['mfa']=False;self.assertEqual(self.result(),'DENY')
 def test_global_admin(self):self.d['requests'][0]['role']='Global Administrator';self.assertEqual(self.result(),'ROLE_REVIEW')
 def test_long_duration(self):self.d['requests'][0]['end']='2026-10-18T14:00:00Z';self.assertEqual(self.result(),'DURATION_REVIEW')
 def test_no_timezone(self):
  self.d['now']='2026-10-18T12:30:00'
  with self.assertRaises(ValueError):evaluate(self.d)
 def test_bad_boolean(self):
  self.d['requests'][0]['mfa']='true'
  with self.assertRaises(ValueError):evaluate(self.d)
if __name__=='__main__':unittest.main()
