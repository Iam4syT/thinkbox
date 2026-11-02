"""SQLite rehearsal of transactional schema change and rollback; not SQL Server."""
import sqlite3
def open_db():
 c=sqlite3.connect(":memory:")
 c.execute("CREATE TABLE tickets (id TEXT PRIMARY KEY, status TEXT NOT NULL)")
 c.execute("INSERT INTO tickets VALUES (?,?)",("SYN-1","New"));c.commit();return c
def release(c,fail=False):
 try:
  c.execute("BEGIN")
  c.execute("ALTER TABLE tickets ADD COLUMN owner TEXT NOT NULL DEFAULT 'unassigned'")
  c.execute("UPDATE tickets SET owner=? WHERE id=?",("operator-a","SYN-1"))
  if fail:raise RuntimeError("Injected release failure")
  c.commit()
 except Exception:
  c.rollback();raise
def get_ticket(c,ticket_id):return c.execute("SELECT * FROM tickets WHERE id=?",(ticket_id,)).fetchone()
def columns(c):return [r[1] for r in c.execute("PRAGMA table_info(tickets)")]
def demo():
 c=open_db();before=columns(c)
 try:release(c,True)
 except RuntimeError:print("Injected failure rolled back:",columns(c)==before)
 release(c);print("Successful release:",get_ticket(c,"SYN-1"));c.close()
if __name__=="__main__":demo()
