import unittest, sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
from search import search
class Checks(unittest.TestCase):
 def fixture(self):return [{"id":"AUDIO","title":"Audio selection","steps":"Check the selected microphone and speaker; ask the remote participant to verify."}]
 def test_cited_match(self):self.assertTrue(search(self.fixture(),"audio").startswith("[AUDIO]"))
 def test_unknown(self):self.assertTrue(search(self.fixture(),"quantum").startswith("NO MATCH"))
 def test_restricted(self):
  for q in ["password","admin","credentials"]:self.assertTrue(search(self.fixture(),q).startswith("ESCALATE"))
 def test_blank(self):
  with self.assertRaises(ValueError):search(self.fixture()," ")
 def test_duplicate(self):
  with self.assertRaises(ValueError):search(self.fixture()*2,"audio")
 def test_missing_field(self):
  with self.assertRaises(ValueError):search([{"id":"A"}],"audio")
 def test_extra_field(self):
  r=self.fixture();r[0]["private"]="x"
  with self.assertRaises(ValueError):search(r,"audio")
 def test_bad_type(self):
  with self.assertRaises(ValueError):search({},"audio")
if __name__=="__main__":unittest.main()
