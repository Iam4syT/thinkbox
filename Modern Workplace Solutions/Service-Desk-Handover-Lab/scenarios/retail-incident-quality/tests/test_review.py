import unittest,sys,json,copy
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from incident import review
class TicketTests(unittest.TestCase):
 def setUp(self):self.d=json.loads((Path(__file__).resolve().parents[1]/'templates/sample.json').read_text())
 def test_priority_and_gaps(self):
  r=review(self.d)['tickets'];self.assertEqual(r[0]['illustrative_priority'],1);self.assertEqual(r[1]['illustrative_priority'],4);self.assertIn('verification',r[1]['review_items'])
 def test_resolution_cannot_hide_missing_confirmation(self):self.assertIn('user_confirmation_pending',review(self.d)['tickets'][1]['review_items'])
 def test_documented(self):
  t=self.d['tickets'][1];t.update(verification='Test sign-in repeated',user_confirmed=True);self.assertEqual(review(self.d)['tickets'][1]['status'],'documented_for_review')
 def test_empty(self):self.d['tickets']=[];self.assertRaises(ValueError,review,self.d)
 def test_duplicate(self):self.d['tickets'].append(copy.deepcopy(self.d['tickets'][0]));self.assertRaises(ValueError,review,self.d)
 def test_boolean_impact(self):self.d['tickets'][0]['impact']=True;self.assertRaises(ValueError,review,self.d)
 def test_out_of_range(self):self.d['tickets'][0]['urgency']=4;self.assertRaises(ValueError,review,self.d)
 def test_unknown_state(self):self.d['tickets'][0]['state']='closed';self.assertRaises(ValueError,review,self.d)
 def test_missing_owner(self):self.d['tickets'][0]['owner']='';self.assertIn('owner',review(self.d)['tickets'][0]['review_items'])
 def test_string_confirmation(self):self.d['tickets'][0]['user_confirmed']='yes';self.assertRaises(ValueError,review,self.d)
 def test_bad_root(self):self.assertRaises(ValueError,review,[])
if __name__=='__main__':unittest.main()
