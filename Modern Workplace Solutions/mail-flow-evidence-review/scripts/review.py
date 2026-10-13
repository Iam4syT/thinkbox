import json,sys
from pathlib import Path
def review(data):
 seen=set();out=[]
 for row in data['items']:
  uid=row['id'];status=row['status'];smtp=row['smtp'];aliases=row['aliases']
  if not uid or uid in seen: raise ValueError('missing or duplicate id')
  seen.add(uid)
  if status not in {'Delivered','Failed','Pending'}: raise ValueError('unsupported status')
  if not isinstance(aliases,list) or not isinstance(smtp,str) or not smtp: raise ValueError('invalid SMTP data')
  reasons=[]
  if status!='Delivered': reasons.append('status-'+status.lower())
  if smtp.lower() not in [x.lower() for x in aliases]: reasons.append('smtp-not-in-aliases')
  out.append({'id':uid,'review_required':bool(reasons),'reasons':reasons,'settings_changed':False})
 return out
if __name__=='__main__': print(json.dumps(review(json.loads(Path(sys.argv[1]).read_text())),indent=2))
