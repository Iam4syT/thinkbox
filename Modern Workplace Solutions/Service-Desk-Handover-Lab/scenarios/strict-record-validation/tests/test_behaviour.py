import importlib.util
from pathlib import Path
import unittest
SPEC=importlib.util.spec_from_file_location("checker",Path(__file__).resolve().parents[1]/"scripts"/"check_ticket.py")
m=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(m)
class Behaviour(unittest.TestCase):
 def setUp(self):self.data={'impact': 'Synthetic impact', 'symptoms': 'Synthetic symptoms', 'checks': 'Synthetic checks', 'result': 'Synthetic result', 'next_owner': 'Synthetic next_owner', 'next_action': 'Synthetic next_action', 'user_update': 'Synthetic user_update', 'security_incident': False}
 def test_valid(self):self.assertEqual(m.inspect_record(self.data)['status'],'COMPLETE')
 def test_missing(self):
  self.data.pop('user_update')
  if m.MODE=='readiness':
   with self.assertRaises(ValueError):m.inspect_record(self.data)
  else:self.assertEqual(m.inspect_record(self.data)['status'],'INCOMPLETE')
 def test_wrong_type(self):
  self.data['user_update']=[]
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
