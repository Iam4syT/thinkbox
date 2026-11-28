import unittest
from check import heartbeat

class HeartbeatTests(unittest.TestCase):
    def test_fresh(self):
        self.assertEqual(heartbeat(2), "fresh")
    def test_boundary(self):
        self.assertEqual(heartbeat(5), "fresh")
    def test_stale(self):
        self.assertEqual(heartbeat(6), "investigate")
    def test_missing(self):
        self.assertEqual(heartbeat(None), "review input")
    def test_bad_clock(self):
        self.assertEqual(heartbeat(-1), "review input")
    def test_nonfinite(self):
        self.assertEqual(heartbeat(float("nan")), "review input")
