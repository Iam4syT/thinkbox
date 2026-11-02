import unittest,sys,json,tempfile
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from main import route,load
ROOT=Path(__file__).resolve().parents[1]
class OfflineContractTests(unittest.TestCase):
 def setUp(self):self.model=load(ROOT/'model/model.json')
 def test_prediction(self):self.assertEqual(route(self.model,'/predict?x=3'),(200,{'prediction':16,'version':'demo-v1','scope':'synthetic_local_only'}))
 def test_health(self):self.assertEqual(route(self.model,'/health')[0],200)
 def test_unknown(self):self.assertEqual(route(self.model,'/admin')[0],404)
 def test_bounds(self):
  for x in ['-1','101','nan','inf','abc','']:self.assertEqual(route(self.model,'/predict?x='+x)[0],400)
 def test_duplicates(self):self.assertEqual(route(self.model,'/predict?x=1&x=2')[0],400)
 def test_extra_field(self):self.assertEqual(route(self.model,'/predict?x=1&email=private')[0],400)
 def test_missing(self):self.assertEqual(route(self.model,'/predict')[0],400)
 def test_no_echo(self):self.assertEqual(route(self.model,'/predict?x=secret')[1],{'error':'invalid input'})
 def test_wrong_version(self):
  with tempfile.TemporaryDirectory() as tmp:
   p=Path(tmp)/'model.json';self.model['version']='unknown';p.write_text(json.dumps(self.model))
   with self.assertRaises(ValueError):load(p)
 def test_nonfinite_coefficient(self):
  with tempfile.TemporaryDirectory() as tmp:
   p=Path(tmp)/'model.json';self.model['slope']=float('inf');p.write_text(json.dumps(self.model))
   with self.assertRaises(ValueError):load(p)
if __name__=='__main__':unittest.main()
