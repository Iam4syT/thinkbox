import hashlib
import unittest
from check import verify_restore

class RestoreTests(unittest.TestCase):
    reference = hashlib.sha256(b"site inventory").hexdigest()
    def test_good(self):
        self.assertEqual(verify_restore(self.reference, b"site inventory"), "verified")
    def test_changed(self):
        self.assertEqual(verify_restore(self.reference, b"site Inventory"), "mismatch")
    def test_missing_file(self):
        self.assertEqual(verify_restore(self.reference, None), "restore unavailable")
    def test_missing_reference(self):
        self.assertEqual(verify_restore("", b"site inventory"), "reference unavailable")
    def test_empty_file(self):
        self.assertEqual(verify_restore(hashlib.sha256(b"").hexdigest(), b""), "verified")
