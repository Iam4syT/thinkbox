import unittest,json,sys,copy
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from review import review
class Behaviour(unittest.TestCase):
 def data(self):return json.loads((Path(__file__).resolve().parents[1]/'fixtures/sample.json').read_text())
 def test_normal(self):self.assertEqual([x['review_required'] for x in review(self.data())],[False,True,True])
 def test_mismatch(self):self.assertIn('smtp-not-in-aliases',review(self.data())[1]['reasons'])
 def test_pending_not_failure(self):self.assertEqual(review(self.data())[2]['reasons'],['status-pending'])
 def test_duplicate(self):
  x=self.data();x['items'].append(x['items'][0]);
  with self.assertRaises(ValueError):review(x)
 def test_unknown(self):
  x=self.data();x['items'][0]['status']='Mystery'
  with self.assertRaises(ValueError):review(x)
 def test_missing(self):
  x=self.data();del x['items'][0]['smtp']
  with self.assertRaises(KeyError):review(x)
 def test_read_only(self):
  x=self.data();before=copy.deepcopy(x);review(x);self.assertEqual(x,before)
