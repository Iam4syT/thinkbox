import copy
import json
import unittest
from pathlib import Path
from main import assess, report

class DiscoveryTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(Path('data/brief.json').read_text())
    def test_complete(self):
        self.assertEqual(assess(self.data), [])
    def test_missing_owner(self):
        del self.data['requirements'][0]['owner']
        self.assertIn('R1: missing owner', assess(self.data))
    def test_retention_unknown(self):
        self.data['retention_days'] = None
        self.assertIn('Unresolved retention_days', assess(self.data))
    def test_invalid_retention(self):
        self.data['retention_days'] = -1
        self.assertIn('retention_days must be a positive integer', assess(self.data))
    def test_duplicate_id(self):
        self.data['requirements'].append(copy.deepcopy(self.data['requirements'][0]))
        with self.assertRaises(ValueError): assess(self.data)
    def test_empty(self):
        self.data['requirements'] = []
        self.assertIn('No requirements recorded', assess(self.data))
    def test_bad_structure(self):
        with self.assertRaises(ValueError): assess({'requirements': 'wrong'})
    def test_human_review_retained(self):
        self.assertIn('human approval still required', report(self.data))
    def test_traceability(self):
        self.assertIn('R2 | Example security reviewer', report(self.data))
    def test_missing_acceptance(self):
        self.data['requirements'][0]['acceptance'] = ' '
        self.assertIn('R1: missing acceptance', assess(self.data))
if __name__ == '__main__': unittest.main()
