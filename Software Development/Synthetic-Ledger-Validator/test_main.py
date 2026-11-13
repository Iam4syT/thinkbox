import tempfile
import unittest
from pathlib import Path

from main import reconcile


class ReconciliationTests(unittest.TestCase):
    def reconcile_text(self, content):
        with tempfile.TemporaryDirectory() as folder:
            file = Path(folder) / "sample.csv"
            file.write_text(content, encoding="utf-8")
            return reconcile(file)

    def test_balanced(self):
        self.assertEqual(self.reconcile_text("id,account,pence\n1,A,25\n2,A,-25\n"), {})

    def test_unbalanced(self):
        self.assertEqual(self.reconcile_text("id,account,pence\n1,A,25\n2,B,-25\n"), {"A": 25, "B": -25})

    def test_duplicate(self):
        with self.assertRaisesRegex(ValueError, "duplicate"):
            self.reconcile_text("id,account,pence\n1,A,25\n1,A,-25\n")

    def test_invalid_amount(self):
        with self.assertRaises(ValueError):
            self.reconcile_text("id,account,pence\n1,A,not-a-number\n")


if __name__ == "__main__":
    unittest.main()
