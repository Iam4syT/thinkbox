import unittest, sys, tempfile, json, subprocess
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from queue_check import analyse
def row(**kw):
 d=dict(id='T1',service='Email',impact='school',urgency='urgent',age_minutes='30');d.update(kw);return d
class QueueTests(unittest.TestCase):
 def test_thresholds(self):
  for impact,urgency,target in [('school','urgent',30),('group','normal',120),('single','normal',480)]:
   for age,expected in [(target-1,False),(target,True),(target+1,True)]:
    with self.subTest(age=age,target=target):
     self.assertEqual(analyse([row(impact=impact,urgency=urgency,age_minutes=str(age))])[0]['overdue'],expected)
 def test_major_requires_both(self):
  self.assertFalse(analyse([row(impact='single')])[0]['major_review'])
  self.assertFalse(analyse([row(urgency='normal')])[0]['major_review'])
  self.assertTrue(analyse([row()])[0]['major_review'])
 def test_bad_inputs(self):
  for rows in [[row(),row()],[row(age_minutes='-1')],[row(age_minutes='later')],[row(impact='unknown')],[{'id':'X'}]]:
   with self.subTest(rows=rows),self.assertRaises(ValueError): analyse(rows)
 def test_order(self):
  self.assertEqual([r['id'] for r in analyse([row(id='B',impact='single',urgency='normal'),row(id='A')])],['A','B'])
 def test_failed_run_preserves_previous_output(self):
  with tempfile.TemporaryDirectory() as d:
   source=Path(d)/'bad.csv'; output=Path(d)/'out.json';output.write_text('previous')
   source.write_text('id,service,impact,urgency,age_minutes\nX,Email,school,urgent,-1\n')
   r=subprocess.run([sys.executable,str(Path(__file__).resolve().parents[1]/'src/queue_check.py'),str(source),str(output)],capture_output=True)
   self.assertEqual(r.returncode,2);self.assertEqual(output.read_text(),'previous')
if __name__=='__main__': unittest.main()
