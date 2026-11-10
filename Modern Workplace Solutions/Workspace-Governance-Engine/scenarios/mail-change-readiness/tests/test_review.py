import unittest
from Scripts.review import REQUIRED, review


class ReviewTests(unittest.TestCase):
    def setUp(self):
        self.complete = dict.fromkeys(REQUIRED, "pass")

    def test_complete(self):
        self.assertEqual(review(self.complete)["decision"], "READY_FOR_REVIEW")

    def test_missing(self):
        del self.complete[REQUIRED[0]]
        result = review(self.complete)
        self.assertEqual(result["decision"], "HOLD")
        self.assertEqual(result["checks"][REQUIRED[0]], "unknown")

    def test_failed(self):
        self.complete[REQUIRED[0]] = "fail"
        self.assertEqual(review(self.complete)["decision"], "HOLD")

    def test_explicit_unknown(self):
        self.complete[REQUIRED[0]] = "unknown"
        self.assertEqual(review(self.complete)["decision"], "HOLD")

    def test_invalid_status(self):
        self.complete[REQUIRED[0]] = ["pass"]
        with self.assertRaises(ValueError):
            review(self.complete)

    def test_extra_key(self):
        self.complete["unapproved"] = "pass"
        with self.assertRaises(ValueError):
            review(self.complete)

    def test_non_object(self):
        with self.assertRaises(ValueError):
            review([])
