import unittest,json,math
from pathlib import Path
from main import review
class Review(unittest.TestCase):
    def record(self):return json.loads((Path(__file__).resolve().parents[1]/'data/example.json').read_text())
    def test_good_is_not_deployment(self):
        r=review(self.record());self.assertEqual(r['decision'],'await_human_review');self.assertFalse(r['deployment_performed'])
    def test_poor_model(self):
        r=self.record();r['model_mae_ms']=20;self.assertEqual(review(r)['decision'],'hold')
    def test_tie_baseline(self):
        r=self.record();r['model_mae_ms']=r['baseline_mae_ms'];self.assertIn('does_not_beat_baseline',review(r)['reasons'])
    def test_missing_privacy(self):
        r=self.record();r['privacy_review']=False;self.assertIn('privacy_review_missing',review(r)['reasons'])
    def test_missing_rollback(self):
        r=self.record();r['rollback_plan']=False;self.assertIn('rollback_plan_missing',review(r)['reasons'])
    def test_data_scope(self):
        r=self.record();r['data_scope']='customer';self.assertEqual(review(r)['decision'],'hold')
    def test_sample_size(self):
        r=self.record();r['test_n']=7;self.assertIn('small_test_set',review(r)['reasons'])
    def test_schema_and_types(self):
        for k,v in [('schema_version',2),('test_n',True),('privacy_review','true'),('model_mae_ms',math.nan)]:
            r=self.record();r[k]=v
            with self.subTest(k=k),self.assertRaises(ValueError):review(r)
        r=self.record();r['extra']='not allowed'
        with self.assertRaises(ValueError):review(r)
    def test_receipt_changes(self):
        a=self.record();b=dict(a,model_id='different');self.assertNotEqual(review(a)['input_sha256'],review(b)['input_sha256'])
if __name__=='__main__':unittest.main()
