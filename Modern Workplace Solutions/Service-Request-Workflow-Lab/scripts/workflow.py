"""Synthetic internal request workflow. No external integrations or authentication."""
import json
from pathlib import Path
ALLOWED={"New":{"Triaged"},"Triaged":{"In progress"},"In progress":{"Resolved"},"Resolved":set()}
class Workflow:
 def __init__(self): self.rows={}
 def add(self,request_id,owner,summary):
  if not request_id or not owner or not summary: raise ValueError("Required field missing")
  if request_id in self.rows: raise ValueError("Duplicate request")
  self.rows[request_id]={"id":request_id,"owner":owner,"summary":summary,"status":"New","version":1}
  return dict(self.rows[request_id])
 def move(self,request_id,status,actor,version):
  row=self.rows[request_id]
  if actor!=row["owner"]: raise PermissionError("Owner required")
  if version!=row["version"]: raise ValueError("Stale version")
  if status not in ALLOWED[row["status"]]: raise ValueError("Invalid transition")
  row["status"]=status;row["version"]+=1
  return dict(row)
 def snapshot(self): return json.loads(json.dumps(self.rows))
def demo():
 w=Workflow();w.add("SYN-001","operator-a","Test account cannot open training site")
 w.move("SYN-001","Triaged","operator-a",1)
 print(json.dumps(w.snapshot(),indent=2))
if __name__=="__main__":demo()
