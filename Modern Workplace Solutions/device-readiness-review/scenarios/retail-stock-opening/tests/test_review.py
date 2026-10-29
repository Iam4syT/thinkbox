import unittest,sys,json,copy
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from readiness import review
class StockTests(unittest.TestCase):
 def setUp(self):self.d=json.loads((Path(__file__).resolve().parents[1]/'templates/sample.json').read_text())
 def test_reservations_and_shortage(self):r=review(self.d);self.assertEqual(r['available']['DEMO-LAPTOP'],2);self.assertEqual(r['shortages'],{'DEMO-LAPTOP':1})
 def test_pending_checks(self):self.assertEqual(set(review(self.d)['pending_checks']),{'device_test','owner_signoff'})
 def test_complete(self):
  self.d['demand']['DEMO-LAPTOP']=2;self.d['checks']={k:True for k in self.d['checks']};self.assertEqual(review(self.d)['status'],'recorded_checks_complete')
 def test_duplicate(self):self.d['stock'].append(copy.deepcopy(self.d['stock'][0]));self.assertRaises(ValueError,review,self.d)
 def test_negative(self):self.d['stock'][0]['on_hand']=-1;self.assertRaises(ValueError,review,self.d)
 def test_bool_quantity(self):self.d['stock'][0]['on_hand']=True;self.assertRaises(ValueError,review,self.d)
 def test_overallocated(self):self.d['stock'][0]['reserved']=8;self.assertRaises(ValueError,review,self.d)
 def test_unknown_sku(self):self.d['demand']['DEMO-MISSING']=2;self.assertEqual(review(self.d)['shortages']['DEMO-MISSING'],2)
 def test_string_check(self):self.d['checks']['device_test']='passed';self.assertRaises(ValueError,review,self.d)
 def test_missing_check(self):del self.d['checks']['network_test'];self.assertRaises(ValueError,review,self.d)
 def test_zero_demand(self):self.d['demand']['DEMO-LAPTOP']=0;self.assertRaises(ValueError,review,self.d)
if __name__=='__main__':unittest.main()
