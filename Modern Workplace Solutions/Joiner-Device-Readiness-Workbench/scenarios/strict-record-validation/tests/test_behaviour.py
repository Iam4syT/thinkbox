import importlib.util
from pathlib import Path
import unittest
SPEC=importlib.util.spec_from_file_location("checker",Path(__file__).resolve().parents[1]/"scripts"/"check_readiness.py")
m=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(m)
class Behaviour(unittest.TestCase):
 def setUp(self):self.data={'os': 'pass', 'account': 'pass', 'network': 'pass', 'software': 'pass', 'peripheral': 'pass'}
 def test_valid(self):self.assertEqual(m.inspect_record(self.data)['status'],'READY')
 def test_missing(self):
  self.data.pop('peripheral')
  if m.MODE=='readiness':
   with self.assertRaises(ValueError):m.inspect_record(self.data)
  else:self.assertEqual(m.inspect_record(self.data)['status'],'INCOMPLETE')
 def test_wrong_type(self):
  self.data['peripheral']=[]
  with self.assertRaises(ValueError):m.inspect_record(self.data)
 def test_extra(self):
  self.data['private_email']='not-permitted'
  with self.assertRaises(ValueError):m.inspect_record(self.data)
 def test_failed_or_security(self):
  if m.MODE=='readiness':
   self.data['network']='fail';self.assertEqual(m.inspect_record(self.data)['status'],'REVIEW')
  else:
   self.data['security_incident']=True;self.assertEqual(m.inspect_record(self.data)['route'],'SECURITY ESCALATION')
 def test_pending_or_missing_security(self):
  if m.MODE=='readiness':
   self.data['software']='pending';self.assertEqual(m.inspect_record(self.data)['status'],'REVIEW')
  else:
   self.data.pop('security_incident')
   with self.assertRaises(ValueError):m.inspect_record(self.data)
 def test_invalid_status_or_string_boolean(self):
  if m.MODE=='readiness':self.data['os']='yes'
  else:self.data['security_incident']='false'
  with self.assertRaises(ValueError):m.inspect_record(self.data)
 def test_non_object(self):
  with self.assertRaises(ValueError):m.inspect_record([])
if __name__=='__main__':unittest.main()
