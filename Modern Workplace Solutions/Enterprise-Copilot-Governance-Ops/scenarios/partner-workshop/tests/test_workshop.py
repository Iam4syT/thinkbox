import unittest,copy
from main import review
class WorkshopTest(unittest.TestCase):
 def setUp(self): self.d={'checks':dict(owner_approved=True,licence_checked=True,baseline_defined=True),'records':[dict(id='finance',classification='Confidential',access_groups=['Finance-Execs'])]}
 def test_normal(self):self.assertEqual(review(self.d)['status'],'bounded_demo_candidate')
 def test_oversharing(self):self.d['records'][0]['access_groups']=['All-Employees'];self.assertEqual(review(self.d)['status'],'review_before_demo')
 def test_unknown_group(self):self.d['records'][0]['access_groups']=['New-Group'];self.assertEqual(review(self.d)['records'][0]['decision'],'review')
 def test_missing_sensitivity(self):del self.d['records'][0]['classification'];self.assertEqual(review(self.d)['status'],'review_before_demo')
 def test_missing_approval(self):del self.d['checks']['owner_approved'];self.assertEqual(review(self.d)['status'],'review_before_demo')
 def test_false_licence(self):self.d['checks']['licence_checked']=False;self.assertEqual(review(self.d)['status'],'review_before_demo')
 def test_false_baseline(self):self.d['checks']['baseline_defined']=False;self.assertEqual(review(self.d)['status'],'review_before_demo')
 def test_bad_bool(self):self.d['checks']['owner_approved']='yes';self.assertRaises(ValueError,review,self.d)
 def test_empty(self):self.d['records']=[];self.assertRaises(ValueError,review,self.d)
 def test_duplicate(self):self.d['records']*=2;self.assertRaises(ValueError,review,self.d)
 def test_no_content(self):self.assertNotIn('content',str(review(self.d)))
 def test_anonymous(self):self.d['records'][0]['access_groups']=['Anonymous'];self.assertEqual(review(self.d)['records'][0]['decision'],'exposed')
if __name__=='__main__':unittest.main()
