import copy,json,unittest
from pathlib import Path
from review import review
class NetworkChecks(unittest.TestCase):
 def setUp(self):self.row=json.loads(Path("sample.json").read_text())
 def test_link_local(self):self.assertTrue(any("DHCP" in x for x in review(self.row)["findings"]))
 def test_unknown_not_pass(self):self.assertEqual(review(self.row)["status"],"needs review")
 def test_dns_failure(self):self.assertIn("dns_ok failed: investigate",review(self.row)["findings"])
 def test_invalid_ip(self):
  self.row["ipv4"]="bad"
  with self.assertRaises(ValueError):review(self.row)
 def test_string_false(self):
  self.row["dns_ok"]="false"
  with self.assertRaises(ValueError):review(self.row)
 def test_no_mutation(self):
  before=copy.deepcopy(self.row);review(self.row);self.assertEqual(before,self.row)
 def test_no_auto_approval(self):
  self.row.update(ipv4="192.0.2.10",gateway="192.0.2.1",dns_ok=True,tcp443_ok=True,physical_check=True,patch_review=True)
  self.assertEqual(review(self.row)["status"],"recorded checks passed");self.assertFalse(review(self.row)["approved_for_deployment"])
 def test_extra_field(self):
  self.row["password"]="fake"
  with self.assertRaises(ValueError):review(self.row)
 def test_missing_field(self):
  del self.row["device"]
  with self.assertRaises(ValueError):review(self.row)
 def test_null_dns(self):
  self.row["dns_ok"]=None;self.assertIn("dns_ok not observed",review(self.row)["findings"])
if __name__=="__main__":unittest.main()
