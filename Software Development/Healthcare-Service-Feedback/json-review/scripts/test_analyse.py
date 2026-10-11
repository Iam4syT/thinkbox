import unittest
from analyse import analyse
class Tests(unittest.TestCase):
 def ticket(self,**kw): return dict(id="T1",theme="access",age_hours=4,target_hours=4,safety_concern=False,**kw)
 def test_boundary_not_overdue(self): self.assertEqual(analyse([self.ticket()])["overdue_ids"],[])
 def test_overdue_and_safety_review(self):
  t=self.ticket();t.update(age_hours=5,safety_concern=True);r=analyse([t]);self.assertEqual(r["overdue_ids"],["T1"]);self.assertEqual(r["human_review_ids"],["T1"])
 def test_unknown_review(self):
  t=self.ticket();t["theme"]="unknown";self.assertEqual(analyse([t])["human_review_ids"],["T1"])
 def test_duplicates_rejected(self):
  with self.assertRaises(ValueError):analyse([self.ticket(),self.ticket()])
 def test_negative_rejected(self):
  t=self.ticket();t["age_hours"]=-1
  with self.assertRaises(ValueError):analyse([t])
 def test_bool_not_hours(self):
  t=self.ticket();t["age_hours"]=True
  with self.assertRaises(ValueError):analyse([t])
 def test_nonlist(self):
  with self.assertRaises(ValueError):analyse({})
 def test_empty(self):self.assertEqual(analyse([])["ticket_count"],0)
