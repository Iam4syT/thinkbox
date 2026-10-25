import importlib.util,unittest
from pathlib import Path
s=importlib.util.spec_from_file_location('check',Path(__file__).parents[1]/'scripts/check.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def row(**kw):
 r=dict(id='DEMO',service='Teams',summary='Example',due='2026-10-29',impact='high',owner='Service-owner',status='draft');r.update(kw);return r
class Behaviour(unittest.TestCase):
 def test_due_soon(self):self.assertEqual(m.analyse([row()],'2026-10-25')['queue'][0]['urgency'],'due soon')
 def test_overdue(self):self.assertEqual(m.analyse([row(due='2026-10-20')],'2026-10-25')['queue'][0]['urgency'],'overdue')
 def test_approval_boundary(self):self.assertEqual(m.analyse([row()],'2026-10-25')['queue'][0]['review'],'owner approval needed')
 def test_missing_owner(self):
  with self.assertRaises(ValueError):m.analyse([row(owner='')],'2026-10-25')
 def test_bad_date(self):
  with self.assertRaises(ValueError):m.analyse([row(due='tomorrow')],'2026-10-25')
 def test_duplicate(self):
  with self.assertRaises(ValueError):m.analyse([row(),row()],'2026-10-25')
 def test_unknown_status(self):
  with self.assertRaises(ValueError):m.analyse([row(status='sent')],'2026-10-25')
if __name__=='__main__':unittest.main()
