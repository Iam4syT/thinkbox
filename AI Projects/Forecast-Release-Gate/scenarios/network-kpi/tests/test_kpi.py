import unittest, math
from main import DATA,evaluate
class KPI(unittest.TestCase):
    def copy(self):return [dict(r) for r in DATA]
    def test_baseline_and_fit(self):
        r=evaluate();self.assertEqual((r['train_n'],r['test_n']),(16,8));self.assertEqual(r['model_mae_ms'],0);self.assertEqual(r['baseline_mae_ms'],9);self.assertEqual(r['review'],'eligible_for_review')
    def test_shift_holds(self):
        rows=self.copy()
        for r in rows[16:]:r['latency_ms']+=20
        self.assertEqual(evaluate(rows)['review'],'hold')
    def test_targets_do_not_leak(self):
        rows=self.copy()
        for r in rows[16:]:r['latency_ms']+=3
        r=evaluate(rows);self.assertEqual((r['slope'],r['intercept']),(2,10));self.assertEqual(r['model_mae_ms'],3)
    def test_duplicate_time(self):
        rows=self.copy();rows[1]['time']=1
        with self.assertRaises(ValueError):evaluate(rows)
    def test_schema(self):
        rows=self.copy();rows[0]['customer_name']='unwanted'
        with self.assertRaises(ValueError):evaluate(rows)
    def test_nonfinite(self):
        for v in [math.nan, math.inf,'3',True]:
            rows=self.copy();rows[0]['load']=v
            with self.subTest(v=v),self.assertRaises(ValueError):evaluate(rows)
    def test_negative(self):
        rows=self.copy();rows[0]['latency_ms']=-1
        with self.assertRaises(ValueError):evaluate(rows)
    def test_constant(self):
        rows=self.copy()
        for r in rows[:16]:r['load']=1
        with self.assertRaises(ValueError):evaluate(rows)
    def test_splits(self):
        for cut in [0,2,24,100,2.5]:
            with self.subTest(cut=cut),self.assertRaises(ValueError):evaluate(cut=cut)
if __name__=='__main__':unittest.main()
