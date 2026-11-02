import sys,unittest,sqlite3
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
from release import open_db,release,get_ticket,columns
class Tests(unittest.TestCase):
 def setUp(self):self.c=open_db()
 def tearDown(self):self.c.close()
 def test_schema_change(self):release(self.c);self.assertIn("owner",columns(self.c))
 def test_values_preserved(self):release(self.c);self.assertEqual(get_ticket(self.c,"SYN-1"),("SYN-1","New","operator-a"))
 def test_failure_rolls_back_schema(self):
  with self.assertRaises(RuntimeError):release(self.c,True)
  self.assertEqual(columns(self.c),["id","status"])
 def test_failure_preserves_data(self):
  with self.assertRaises(RuntimeError):release(self.c,True)
  self.assertEqual(get_ticket(self.c,"SYN-1"),("SYN-1","New"))
 def test_retry_after_failure(self):
  with self.assertRaises(RuntimeError):release(self.c,True)
  release(self.c);self.assertIn("owner",columns(self.c))
 def test_duplicate_release_fails_without_corruption(self):
  release(self.c)
  with self.assertRaises(sqlite3.OperationalError):release(self.c)
  self.assertEqual(get_ticket(self.c,"SYN-1")[2],"operator-a")
 def test_parameterised_lookup(self):self.assertIsNone(get_ticket(self.c,"x' OR 1=1 --"))
 def test_backup_restore(self):
  backup=sqlite3.connect(":memory:");self.c.backup(backup);release(self.c);backup.backup(self.c);backup.close()
  self.assertEqual(columns(self.c),["id","status"]);self.assertEqual(get_ticket(self.c,"SYN-1"),("SYN-1","New"))
if __name__=="__main__":unittest.main()
