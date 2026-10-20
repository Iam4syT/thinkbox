import unittest,copy
from main import review,run
from pathlib import Path
import tempfile,json
class Checks(unittest.TestCase):
 def setUp(self): self.row=dict(id="x",licence="yes",service_health="healthy",access="scoped",label="confidential",encrypted=False)
 def test_label_is_not_enforcement(self): self.assertTrue(review(self.row)["label_is_not_enforcement"]); self.assertFalse(review(self.row)["authorises_change"])
 def test_oversharing(self): self.row["access"]="broad"; self.assertIn("review_oversharing",review(self.row)["reasons"])
 def test_unknown_never_clean(self): self.row["access"]="unknown"; self.assertIn("collect_evidence",review(self.row)["reasons"])
 def test_licence(self): self.row["licence"]="no"; self.assertIn("check_licence",review(self.row)["reasons"])
 def test_service(self): self.row["service_health"]="incident"; self.assertIn("check_service_incident",review(self.row)["reasons"])
 def test_invalid(self): self.row["access"]="everyone"; self.assertRaises(ValueError,review,self.row)
 def test_missing(self): del self.row["label"]; self.assertRaises(ValueError,review,self.row)
 def test_duplicate_rejected(self):
  with tempfile.TemporaryDirectory() as t:
   p=Path(t)/"in.json"; p.write_text(json.dumps([self.row,self.row])); self.assertRaises(ValueError,run,p,Path(t)/"out.json")
if __name__=="__main__":unittest.main()
