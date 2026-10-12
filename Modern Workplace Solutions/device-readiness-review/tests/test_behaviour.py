import unittest,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from review import review
class Behaviour(unittest.TestCase):
 def row(self): return dict(serial='D1',os='macOS',owner='demo',managed=True,encrypted=True,patched=True)
 def test_ready(self): self.assertEqual(review([self.row()])[0]['status'],'ready-for-human-check')
 def test_unmanaged(self):
  x=self.row();x['managed']=False;self.assertIn('managed-check-required',review([x])[0]['issues'])
 def test_owner(self):
  x=self.row();x['owner']='';self.assertTrue(review([x])[0]['ticket_required'])
 def test_patch(self):
  x=self.row();x['patched']=False;self.assertIn('patched-check-required',review([x])[0]['issues'])
 def test_duplicate(self):
  with self.assertRaises(ValueError): review([self.row(),self.row()])
 def test_os(self):
  x=self.row();x['os']='unknown'
  with self.assertRaises(ValueError): review([x])
 def test_boolean(self):
  x=self.row();x['encrypted']='yes'
  with self.assertRaises(ValueError): review([x])
 def test_no_mutation(self):
  x=self.row();review([x]);self.assertEqual(x,self.row())
