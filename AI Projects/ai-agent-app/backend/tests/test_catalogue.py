import unittest
from main import app

class CatalogueTests(unittest.TestCase):
    def test_offline_catalogue(self):
        with app.test_client() as client:
            result = client.get('/api/portfolio')
            self.assertEqual(result.status_code, 200)
            for project in result.json['projects']:
                self.assertTrue(project['url'].startswith('https://github.com/Iam4syT/thinkbox/'))
            result = client.post('/api/project', json={'message':'list projects'})
            self.assertIn('Copilot Governance', result.json['response'])
            result = client.post('/api/career', json={'message':'experience'})
            self.assertIn('Ongoing', result.json['response'])
            self.assertNotIn('Tech Innovations', result.json['response'])
