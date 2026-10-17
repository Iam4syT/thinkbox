import sys,json,unittest,copy
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from triage import triage
P=Path(__file__).resolve().parents[1];NOW='2026-01-01T10:00:00+00:00'
class TriageTests(unittest.TestCase):
 def setUp(self): self.e=json.loads((P/'templates/events.json').read_text())
 def test_repeat_grouped(self):self.assertEqual(triage(self.e,NOW)['groups'][0]['count'],2)
 def test_unknown_critical_escalated(self):
  x=triage(self.e,NOW)['groups'][1];self.assertTrue(x['urgent']);self.assertEqual(x['owner'],'specialist review')
 def test_old_information_excluded(self):self.assertEqual(triage(self.e,NOW)['excluded'],2)
 def test_no_auto_fix(self):self.assertFalse(triage(self.e,NOW)['remediation_performed'])
 def test_duplicate_rejected(self):
  with self.assertRaises(ValueError):triage(self.e+[copy.deepcopy(self.e[0])],NOW)
 def test_future_rejected(self):
  self.e[0]['time']='2027-01-01T10:00:00+00:00'
  with self.assertRaises(ValueError):triage(self.e,NOW)
 def test_missing_timezone_rejected(self):
  with self.assertRaises(ValueError):triage(self.e,'2026-01-01T10:00:00')
 def test_invalid_severity_rejected(self):
  self.e[0]['level']='OK'
  with self.assertRaises(ValueError):triage(self.e,NOW)
 def test_missing_field_rejected(self):
  del self.e[0]['host']
  with self.assertRaises(ValueError):triage(self.e,NOW)
if __name__=='__main__':unittest.main()
