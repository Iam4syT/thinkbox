import unittest
from triage import classify,transition
class Tests(unittest.TestCase):
    def setUp(self): self.t={'id':'TEST','critical_service':True,'workaround':False,'users':1,'channel':'phone','summary':'Synthetic service unavailable'}
    def test_priority(self):
        self.assertEqual(classify(self.t)['priority'],'P1')
        self.assertEqual(classify({**self.t,'critical_service':False,'users':5})['priority'],'P2')
        self.assertEqual(classify({**self.t,'critical_service':False})['priority'],'P3')
    def test_invalid_impact(self):
        for value in ['false',None,0]:
            with self.assertRaises(ValueError): classify({**self.t,'critical_service':value})
    def test_empty_summary(self):
        with self.assertRaises(ValueError): classify({**self.t,'summary':''})
    def test_owner_required(self):
        with self.assertRaises(ValueError): transition(classify(self.t),'assigned','note')
    def test_no_direct_closure(self):
        with self.assertRaises(ValueError): transition(classify(self.t),'closed','note',verified=True)
    def test_resolution_verification(self):
        t=transition(classify(self.t),'assigned','taken','analyst')
        with self.assertRaises(ValueError):transition(t,'resolved','fixed')
        t=transition(t,'resolved','synthetic retest passed',verified=True)
        self.assertEqual(transition(t,'closed','synthetic user confirms',verified=True)['state'],'closed')
    def test_escalation_preserves_owner(self):
        t=transition(classify(self.t),'assigned','taken','analyst')
        self.assertEqual(transition(t,'escalated','specialist needed')['owner'],'analyst')
if __name__=='__main__': unittest.main()
