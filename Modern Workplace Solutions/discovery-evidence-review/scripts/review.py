import json,hashlib,sys
from pathlib import Path
def review(data):
 token=data['token'];allowed=data['allowed_mailboxes'];seen=set();out=[]
 if not isinstance(token,str) or not token.strip(): raise ValueError('missing query token')
 if not isinstance(allowed,list) or not allowed: raise ValueError('missing mailbox scope')
 for row in data['items']:
  uid=row['id'];mailbox=row['mailbox'];subject=row['subject']
  if not uid or uid in seen: raise ValueError('missing or duplicate id')
  seen.add(uid)
  if mailbox in allowed and token.lower() in subject.lower():
   out.append({'id':uid,'sha256':hashlib.sha256(json.dumps(row,sort_keys=True).encode()).hexdigest()})
 return out
if __name__=='__main__': print(json.dumps(review(json.loads(Path(sys.argv[1]).read_text())),indent=2))
