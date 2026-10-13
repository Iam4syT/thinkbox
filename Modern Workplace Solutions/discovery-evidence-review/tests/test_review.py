import unittest,json,sys,copy
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from review import review
class Behaviour(unittest.TestCase):
 def data(self):return json.loads((Path(__file__).resolve().parents[1]/'fixtures/sample.json').read_text())
 def test_scoped(self):self.assertEqual([x['id'] for x in review(self.data())],['e1'])
 def test_case(self):
  x=self.data();x['token']='demo-case-17';self.assertEqual(len(review(x)),1)
 def test_empty_query(self):
  x=self.data();x['token']=''
  with self.assertRaises(ValueError):review(x)
 def test_empty_scope(self):
  x=self.data();x['allowed_mailboxes']=[]
  with self.assertRaises(ValueError):review(x)
 def test_duplicate(self):
  x=self.data();x['items'].append(x['items'][0])
  with self.assertRaises(ValueError):review(x)
 def test_hash_changes(self):
  x=self.data();old=review(x)[0]['sha256'];x['items'][0]['subject']+=' changed';self.assertNotEqual(old,review(x)[0]['sha256'])
 def test_unchanged(self):
  x=self.data();old=copy.deepcopy(x);review(x);self.assertEqual(x,old)
