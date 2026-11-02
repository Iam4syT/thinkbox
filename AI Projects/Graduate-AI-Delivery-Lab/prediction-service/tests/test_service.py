import unittest,sys,json,threading,tempfile
from urllib.request import urlopen
from urllib.error import HTTPError
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from main import server,load,predict
ROOT=Path(__file__).resolve().parents[1]
class ServiceTests(unittest.TestCase):
 @classmethod
 def setUpClass(c):
  
  try:c.srv=server(ROOT/'model/model.json')
  except PermissionError as error:raise unittest.SkipTest('Loopback socket blocked by host permissions: '+str(error))
  c.thread=threading.Thread(target=c.srv.serve_forever,daemon=True);c.thread.start();c.base='http://127.0.0.1:'+str(c.srv.server_port)
 @classmethod
 def tearDownClass(c):c.srv.shutdown();c.srv.server_close();c.thread.join()
 def get(self,p):
  try:
   with urlopen(self.base+p,timeout=3) as r:return r.status,json.load(r)
  except HTTPError as r:return r.code,json.load(r)
 def test_health(self):self.assertEqual(self.get('/health')[0],200)
 def test_predict(self):self.assertEqual(self.get('/predict?x=3')[1]['prediction'],16)
 def test_unknown_route(self):self.assertEqual(self.get('/admin')[0],404)
 def test_invalid_range(self):
  for x in ['-1','101','nan','inf','abc','']:self.assertEqual(self.get('/predict?x='+x)[0],400)
 def test_missing_and_duplicate(self):
  for q in ['','x=1&x=2','x=1&email=private']:self.assertEqual(self.get('/predict?'+q)[0],400)
 def test_no_input_echo(self):self.assertEqual(self.get('/predict?x=secret')[1],{'error':'invalid input'})
 def test_loopback(self):self.assertEqual(self.srv.server_address[0],'127.0.0.1')
 def test_bad_model(self):
  with tempfile.TemporaryDirectory() as tmp:
   p=Path(tmp)/'bad.json';p.write_text('{"version":"unknown"}')
   with self.assertRaises(ValueError):load(p)
 def test_monitoring_counts(self):
  old=self.srv.counts.get('200',0);self.get('/health');self.assertEqual(self.srv.counts['200'],old+1)
 def test_bool_coefficient(self):
  with tempfile.TemporaryDirectory() as tmp:
   p=Path(tmp)/'model.json';d=load(ROOT/'model/model.json');d['slope']=True;p.write_text(json.dumps(d))
   with self.assertRaises(ValueError):load(p)
if __name__=='__main__':unittest.main()
