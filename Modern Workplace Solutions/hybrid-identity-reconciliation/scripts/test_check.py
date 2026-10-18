import unittest,copy,json
from pathlib import Path
from check import evaluate
class Behaviour(unittest.TestCase):
 def setUp(self):self.d=json.loads((Path(__file__).parents[1]/'templates/sample.json').read_text())
 def test_normal(self):self.assertEqual(evaluate(self.d)['status'],'CHECKS_PASS')
 def test_casefold(self):self.d['cloud'][0]['smtp']='PERSON@example.invalid';self.assertEqual(evaluate(self.d)['status'],'CHECKS_PASS')
 def test_missing(self):self.d['cloud']=[];self.assertEqual(evaluate(self.d)['findings'][0]['result'],'MISSING')
 def test_duplicate(self):self.d['cloud'].append(dict(self.d['cloud'][0],id='c2'));self.assertEqual(evaluate(self.d)['findings'][0]['result'],'AMBIGUOUS')
 def test_unsynced(self):self.d['cloud'][0]['synced']=False;self.assertEqual(evaluate(self.d)['findings'][0]['result'],'UNSYNCED')
 def test_disabled(self):self.d['onprem'][0]['enabled']=False;self.assertEqual(evaluate(self.d)['findings'][0]['result'],'DISABLED_REVIEW')
 def test_string_boolean(self):
  self.d['onprem'][0]['enabled']='false'
  with self.assertRaises(ValueError):evaluate(self.d)
 def test_no_mutation(self):before=copy.deepcopy(self.d);evaluate(self.d);self.assertEqual(self.d,before)
if __name__=='__main__':unittest.main()
