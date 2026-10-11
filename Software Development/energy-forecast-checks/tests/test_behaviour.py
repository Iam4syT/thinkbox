import unittest, tempfile
from pathlib import Path
from src.engine import load, evaluate

class Behaviour(unittest.TestCase):
 def test_baseline_and_split(self):
  r=evaluate([(i,100+5*i) for i in range(12)])
  self.assertEqual((r["train_rows"],r["test_rows"]),(8,4))
  self.assertEqual(r["persistence_mae_kw"],5);self.assertAlmostEqual(r["trend_mae_kw"],0)
 def test_future_does_not_change_fit(self):
  rows=[(i,100+5*i) for i in range(12)];a=evaluate(rows)
  rows[11]=(11,900);b=evaluate(rows)
  self.assertEqual((a["slope"],a["intercept"]),(b["slope"],b["intercept"]))
 def check_bad(self,text):
  with tempfile.TemporaryDirectory() as t:
   p=Path(t)/"bad.csv";p.write_text(text)
   with self.assertRaises(ValueError):load(p)
 def test_bad_header(self):self.check_bad("time,value\n0,1\n")
 def test_negative(self):self.check_bad("hour,demand_kw\n0,-1\n")
 def test_nonfinite(self):self.check_bad("hour,demand_kw\n0,nan\n")
 def test_order(self):self.check_bad("hour,demand_kw\n"+"\n".join(f"{i},10" for i in [0,1,2,2,4,5]))
 def test_short(self):self.check_bad("hour,demand_kw\n0,10\n1,15\n")
 def test_valid_file(self):self.assertEqual(len(load("data/demand.csv")),12)
