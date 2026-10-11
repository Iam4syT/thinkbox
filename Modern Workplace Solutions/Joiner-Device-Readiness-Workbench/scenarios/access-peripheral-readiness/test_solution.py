import copy, json, unittest
from solution import analyse
class Checks(unittest.TestCase):
 def setUp(self):self.rows=json.loads(__import__('pathlib').Path('sample.json').read_text())
 def test_ready(self):self.assertEqual(analyse(self.rows)[0]['status'],'review_ready')
 def test_missing_approval(self):self.assertEqual(analyse(self.rows)[1]['findings'],['Missing approval'])
 def test_disabled(self):self.assertEqual(analyse(self.rows)[2]['status'],'hold')
 def test_privilege(self):self.assertIn('Privilege',analyse(self.rows)[3]['findings'][0])
 def test_missing_peripheral(self):self.assertEqual(analyse(self.rows)[4]['findings'],['Unverified peripheral_test'])
 def test_not_live_permission(self):self.assertTrue(all(r['mode']=='dry_run' for r in analyse(self.rows)))
 def test_reject_duplicate(self):
  self.rows[1]['id']=self.rows[0]['id']
  with self.assertRaises(ValueError):analyse(self.rows)
 def test_reject_empty(self):
  with self.assertRaises(ValueError):analyse([])
 def test_reject_missing_asset(self):
  del self.rows[0]['asset']
  with self.assertRaises(ValueError):analyse(self.rows)
 def test_reject_string_approval(self):
  self.rows[0]['approved']='yes'
  with self.assertRaises(ValueError):analyse(self.rows)
 def test_no_mutation(self):
  old=copy.deepcopy(self.rows);analyse(self.rows);self.assertEqual(old,self.rows)
 def test_deterministic(self):self.assertEqual(analyse(self.rows),analyse(self.rows))
if __name__=='__main__':unittest.main()
