import unittest
from main import Workflow
class WorkflowTests(unittest.TestCase):
    def setUp(self):self.w=Workflow();self.w.submit('1','a','b')
    def approve(self):self.w.decide('1','b',True)
    def test_no_unapproved_write(self):
        with self.assertRaises(PermissionError):self.w.dispatch('1')
    def test_wrong_approver(self):
        with self.assertRaises(PermissionError):self.w.decide('1','c',True)
    def test_self_approval(self):
        with self.assertRaises(ValueError):self.w.submit('2','a','a')
    def test_duplicate_submit(self):self.w.submit('1','c','d');self.assertEqual(self.w.states['1']['requester'],'a')
    def test_success(self):self.approve();self.assertEqual(self.w.dispatch('1')['status'],'complete')
    def test_duplicate_dispatch(self):self.approve();self.w.dispatch('1');self.assertTrue(self.w.dispatch('1')['replayed'])
    def test_reject_blocks(self):
        self.w.decide('1','b',False)
        with self.assertRaises(PermissionError):self.w.dispatch('1')
    def test_403_stops(self):self.approve();self.assertEqual(self.w.dispatch('1',403)['status'],'blocked')
    def test_429_records_delay(self):self.approve();self.assertEqual(self.w.dispatch('1',429,7)['retry_after_seconds'],7)
    def test_bounded_retries(self):
        self.approve()
        for _ in range(3):self.w.dispatch('1',429,1)
        self.assertEqual(self.w.dispatch('1',429,1)['status'],'failed')
    def test_malformed_delay(self):self.approve();self.assertGreater(self.w.dispatch('1',429,'bad')['retry_after_seconds'],0)
    def test_repeat_decision(self):
        self.approve()
        with self.assertRaises(ValueError):self.approve()
if __name__=='__main__':unittest.main()
