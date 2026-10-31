import unittest,copy
from main import search
from pathlib import Path
import json
class Retrieval(unittest.TestCase):
 def setUp(self): self.docs=json.loads(Path("data/documents.json").read_text())
 def test_public(self): self.assertEqual([h["id"] for h in search(self.docs,"visitor","retention")["results"]],["PUBLIC"])
 def test_alpha(self): self.assertEqual({h["id"] for h in search(self.docs,"reader-a","retention")["results"]},{"PUBLIC","A"})
 def test_beta(self): self.assertEqual({h["id"] for h in search(self.docs,"reader-b","retention")["results"]},{"PUBLIC","B"})
 def test_unknown_role(self): self.assertRaises(ValueError,search,self.docs,"admin","retention")
 def test_empty_query(self): self.assertRaises(ValueError,search,self.docs,"visitor","")
 def test_unanswerable(self): self.assertEqual(search(self.docs,"visitor","unicornxyz")["status"],"ABSTAIN")
 def test_duplicate(self): self.assertRaises(ValueError,search,self.docs+[self.docs[0]],"visitor","retention")
 def test_malformed_acl(self): self.docs[0]["groups"]="public";self.assertRaises(ValueError,search,self.docs,"visitor","retention")
 def test_missing_acl_denied(self): del self.docs[0]["groups"];self.assertEqual(search(self.docs,"visitor","retention")["results"],[])
 def test_chunk_acl(self): self.docs[1]["text"]+="\n\nMore retention details";self.assertNotIn("A",str(search(self.docs,"visitor","retention")["results"]))
 def test_citation(self): self.assertEqual(search(self.docs,"visitor","retention")["results"][0]["source"],"synthetic/public-policy")
 def test_long_query(self): self.assertRaises(ValueError,search,self.docs,"visitor","a"*1001)
