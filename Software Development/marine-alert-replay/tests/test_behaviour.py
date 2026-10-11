from pathlib import Path
import unittest, json, math
from src.engine import assess
class Behaviour(unittest.TestCase):
 def row(self,**kw):return {"age_seconds":1,"temperature_c":60,"speed_knots":8,**kw}
 def test_nominal(self):self.assertEqual(assess(self.row())["recommendation"],"REVIEW")
 def test_stale(self):self.assertEqual(assess(self.row(age_seconds=6))["recommendation"],"HOLD")
 def test_heat(self):self.assertEqual(assess(self.row(temperature_c=81))["recommendation"],"HOLD")
 def test_speed(self):self.assertEqual(assess(self.row(speed_knots=13))["recommendation"],"HOLD")
 def test_boundaries(self):self.assertEqual(assess(self.row(age_seconds=5,temperature_c=80,speed_knots=12))["recommendation"],"REVIEW")
 def test_invalid(self):
  for v in [None,-1,True,"8",float("nan"),float("inf")]:
   with self.subTest(value=v):self.assertEqual(assess(self.row(speed_knots=v))["recommendation"],"HOLD")
 def test_no_actuation(self):
  for r in [self.row(),self.row(speed_knots=20),{}]:self.assertFalse(assess(r)["actuation"])
 def test_replay(self):
  rows=json.loads(Path("data/scenarios.json").read_text())
  self.assertEqual(len(rows),5)
  for r in rows:self.assertEqual(assess(r)["recommendation"],r["expected"])
