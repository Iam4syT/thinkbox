import unittest,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from review import review
class Behaviour(unittest.TestCase):
 def row(self,**kw): return dict(id='a',department='IT',active=True,groups=['all-staff'],**kw)
 def test_joiner(self): self.assertEqual(review([self.row()])[0]['add'],['it-tools'])
 def test_leaver(self):
  x=self.row();x['active']=False;self.assertEqual(review([x])[0]['remove'],['all-staff'])
 def test_mover(self):
  x=self.row();x['groups']=['all-staff','support-tools'];self.assertEqual(review([x])[0]['remove'],['support-tools'])
 def test_no_change(self):
  x=self.row();x['groups'].append('it-tools');self.assertEqual(review([x])[0]['action'],'no-change')
 def test_duplicate(self):
  with self.assertRaises(ValueError): review([self.row(),self.row()])
 def test_unknown(self):
  x=self.row();x['department']='Sales'
  with self.assertRaises(ValueError): review([x])
 def test_bad_boolean(self):
  x=self.row();x['active']='false'
  with self.assertRaises(ValueError): review([x])
 def test_input_preserved(self):
  x=self.row();review([x]);self.assertEqual(x['groups'],['all-staff'])
