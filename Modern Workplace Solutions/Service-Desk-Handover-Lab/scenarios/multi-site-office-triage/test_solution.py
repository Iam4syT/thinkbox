import copy, json, unittest
from solution import analyse
class Checks(unittest.TestCase):
 def setUp(self):self.rows=json.loads(__import__('pathlib').Path('sample.json').read_text())
 def test_policy_and_order(self):
  o=analyse(self.rows);self.assertEqual([(r['id'],r['priority']) for r in o['tickets']],[('OFF-03','P1'),('OFF-04','P1'),('OFF-02','P2'),('OFF-01','P3')])
 def test_security_overrides_workaround(self):self.assertIn('Security',analyse(self.rows)['tickets'][0]['next_action'])
 def test_boundary(self):
  self.rows[0]['users']=5;self.assertEqual(next(r for r in analyse(self.rows)['tickets'] if r['id']=='OFF-01')['priority'],'P2')
 def test_owner_and_no_auto_close(self):self.assertTrue(all(r['owner'] and r['state']=='open' for r in analyse(self.rows)['tickets']))
 def test_repeat_signal(self):self.assertEqual(analyse(self.rows)['repeat_categories'],{'mail':2})
 def test_reject_duplicate(self):
  self.rows[1]['id']=self.rows[0]['id']
  with self.assertRaises(ValueError):analyse(self.rows)
 def test_reject_empty(self):
  with self.assertRaises(ValueError):analyse([])
 def test_reject_boolean_count(self):
  self.rows[0]['users']=True
  with self.assertRaises(ValueError):analyse(self.rows)
 def test_reject_unknown_category(self):
  self.rows[0]['category']='secret'
  with self.assertRaises(ValueError):analyse(self.rows)
 def test_reject_missing_field(self):
  del self.rows[0]['workaround']
  with self.assertRaises(ValueError):analyse(self.rows)
 def test_no_input_mutation(self):
  before=copy.deepcopy(self.rows);analyse(self.rows);self.assertEqual(before,self.rows)
 def test_deterministic(self):self.assertEqual(analyse(self.rows),analyse(self.rows))
if __name__=='__main__':unittest.main()
