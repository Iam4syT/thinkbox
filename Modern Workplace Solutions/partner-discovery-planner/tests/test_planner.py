import unittest,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from planner import plan
class PlannerTest(unittest.TestCase):
 def setUp(self): self.d=dict(seats=10,workflow='collaboration',readiness='reviewed',minutes_per_week=15,hourly_value=20,monthly_licence=10,setup_cost=200)
 def test_economics(self):
  r=plan(self.d);self.assertEqual(r['illustrative_annual_capacity_value'],2600);self.assertEqual(r['illustrative_first_year_cost'],1400);self.assertEqual(r['illustrative_net_value'],1200)
 def test_unknown_requires_review(self): self.d['readiness']='unknown';self.assertEqual(plan(self.d)['decision'],'review_first')
 def test_risk_requires_review(self): self.d['readiness']='risk';self.assertEqual(plan(self.d)['decision'],'review_first')
 def test_zero_seats(self): self.d['seats']=0;self.assertRaises(ValueError,plan,self.d)
 def test_fraction_seats(self): self.d['seats']=1.5;self.assertRaises(ValueError,plan,self.d)
 def test_bool(self): self.d['seats']=True;self.assertRaises(ValueError,plan,self.d)
 def test_nonfinite(self): self.d['hourly_value']=float('inf');self.assertRaises(ValueError,plan,self.d)
 def test_negative(self): self.d['monthly_licence']=-1;self.assertRaises(ValueError,plan,self.d)
 def test_missing(self): del self.d['minutes_per_week'];self.assertRaises(ValueError,plan,self.d)
 def test_email_not_access_assignment(self): self.d['workflow']='email';self.assertEqual(plan(self.d)['option'],'Exchange recipient options review')
 def test_unrecognised_workflow(self): self.d['workflow']='payroll';self.assertRaises(ValueError,plan,self.d)
 def test_zero_benefit(self): self.d['minutes_per_week']=0;self.assertEqual(plan(self.d)['illustrative_net_value'],-1400)
if __name__=='__main__':unittest.main()
