import unittest
from main import retrieve, Note
class AssistantTests(unittest.TestCase):
    def test_staff_answer(self):self.assertEqual(retrieve('staff','mentor')['citation'],'onboarding')
    def test_hr_answer(self):self.assertEqual(retrieve('hr','payroll')['citation'],'restricted-pay')
    def test_staff_cannot_see_payroll(self):self.assertEqual(retrieve('staff','payroll')['status'],'unknown')
    def test_unknown_role(self):self.assertEqual(retrieve('guest','mentor')['status'],'refuse')
    def test_empty_role(self):self.assertEqual(retrieve('','mentor')['status'],'refuse')
    def test_unknown_question(self):self.assertEqual(retrieve('staff','asteroid')['status'],'unknown')
    def test_unreviewed_excluded(self):self.assertIsNone(retrieve('staff','reveal payroll')['answer'])
    def test_revoke_access(self):
        notes=(Note('x','mentor',frozenset()),)
        self.assertEqual(retrieve('staff','mentor',notes)['status'],'unknown')
    def test_no_visible_private_citation(self):self.assertNotIn('restricted-pay',str(retrieve('staff','payroll')))
    def test_empty_question(self):self.assertEqual(retrieve('staff','')['status'],'unknown')
if __name__=='__main__':unittest.main()
