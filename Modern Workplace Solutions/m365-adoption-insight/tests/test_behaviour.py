import importlib.util,unittest
from pathlib import Path
s=importlib.util.spec_from_file_location('check',Path(__file__).parents[1]/'scripts/check.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def row(**kw):
 r=dict(cohort='A',service='Teams',licensed='10',active='5',previous_licensed='10',previous_active='4',period_days='30');r.update(kw);return r
class Behaviour(unittest.TestCase):
 def test_rate(self):self.assertEqual(m.analyse([row()])['findings'][0]['change_percentage_points'],10)
 def test_zero(self):self.assertEqual(m.analyse([row(licensed='0',active='0')])['findings'][0]['state'],'suppressed')
 def test_small_prior(self):self.assertNotIn('active_rate_percent',m.analyse([row(previous_licensed='3',previous_active='1')])['findings'][0])
 def test_overcount(self):
  with self.assertRaises(ValueError):m.analyse([row(active='11')])
 def test_negative(self):
  with self.assertRaises(ValueError):m.analyse([row(active='-1')])
 def test_mismatched_window(self):
  with self.assertRaises(ValueError):m.analyse([row(period_days='7')])
 def test_duplicate(self):
  with self.assertRaises(ValueError):m.analyse([row(),row()])
if __name__=='__main__':unittest.main()
