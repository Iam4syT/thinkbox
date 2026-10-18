import math,unittest
from main import DATA,train,rmse,run
class ForecastTests(unittest.TestCase):
 def test_fit_and_holdout(self):
  r=run();self.assertEqual(r['release'],'pass');self.assertLess(r['model_rmse'],r['baseline_rmse']);self.assertEqual(r['holdout_n'],4)
 def test_shift_holds_release(self):self.assertEqual(run(drift=10)['release'],'hold')
 def test_reversed_dates_rejected(self):
  with self.assertRaises(ValueError):run(list(reversed(DATA)))
 def test_constant_feature_rejected(self):
  with self.assertRaises(ValueError):train([{'feature':1,'target':2},{'feature':1,'target':3}])
 def test_non_finite_rejected(self):
  with self.assertRaises(ValueError):train([{'feature':1,'target':2},{'feature':2,'target':float('nan')}])
 def test_split_and_lengths(self):
  with self.assertRaises(ValueError):run(cut=12)
  with self.assertRaises(ValueError):rmse([1],[])
if __name__=='__main__':unittest.main()
