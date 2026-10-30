import unittest
from main import evaluate, CHECKS
class Behaviour(unittest.TestCase):
    def row(self): return dict(id='DEMO-01',**{k:True for k in CHECKS})
    def test_all_true_needs_human(self): self.assertEqual(evaluate([self.row()])[0]['status'],'READY_FOR_HUMAN_REVIEW')
    def test_each_false_holds(self):
        for key in CHECKS:
            row=self.row();row[key]=False;result=evaluate([row])[0]
            self.assertEqual(result['status'],'HOLD'); self.assertEqual(result['failed'],[key])
    def test_each_missing_needs_review(self):
        for key in CHECKS:
            row=self.row();del row[key];self.assertEqual(evaluate([row])[0]['status'],'REVIEW')
    def test_each_null_needs_review(self):
        for key in CHECKS:
            row=self.row();row[key]=None;self.assertEqual(evaluate([row])[0]['status'],'REVIEW')
    def test_duplicate_rejected(self):
        with self.assertRaises(ValueError):evaluate([self.row(),self.row()])
    def test_string_true_rejected(self):
        row=self.row();row[CHECKS[0]]='true'
        with self.assertRaises(ValueError): evaluate([row])
    def test_empty_rejected(self):
        with self.assertRaises(ValueError): evaluate([])
    def test_unknown_field_rejected(self):
        row=self.row();row['aprroved']=True
        with self.assertRaises(ValueError):evaluate([row])
    def test_failure_takes_priority_over_missing(self):
        row=self.row(); row[CHECKS[0]]=False; del row[CHECKS[1]]
        self.assertEqual(evaluate([row])[0]['status'],'HOLD')
if __name__=='__main__':unittest.main(verbosity=2)
