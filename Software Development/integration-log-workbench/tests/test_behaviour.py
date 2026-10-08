import unittest
from src.main import diagnose
class DiagnosisTests(unittest.TestCase):
 def row(self,t='a',rid='1',status=200,accepted=1): return dict(tenant=t,request_id=rid,status=status,accepted=accepted)
 def test_tenant_isolation(self): self.assertEqual(diagnose([self.row(),self.row('b','2',401)],'a')['counts'],{200:1})
 def test_parameter_binding(self): self.assertEqual(diagnose([self.row()],"a' OR 1=1 --")['counts'],{})
 def test_duplicate_retry(self): self.assertEqual(diagnose([self.row(),self.row()],'a')['counts'],{200:1})
 def test_auth_fault(self): self.assertIn('Authentication',diagnose([self.row(status=401)],'a')['findings'][0])
 def test_rate_fault(self): self.assertIn('Throttled',diagnose([self.row(status=429)],'a')['findings'][0])
 def test_server_fault(self): self.assertIn('Server error',diagnose([self.row(status=503)],'a')['findings'][0])
 def test_ingestion_gap(self): self.assertEqual(diagnose([self.row(accepted=0)],'a')['unaccepted_success'],1)
 def test_invalid_input(self):
  with self.assertRaises(ValueError): diagnose([self.row(status='200')],'a')
 def test_empty(self): self.assertIn('No data',diagnose([],'a')['findings'][0])
