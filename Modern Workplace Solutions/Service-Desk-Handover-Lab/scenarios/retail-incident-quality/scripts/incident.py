"""Read-only synthetic ticket-quality exercise; not a ServiceNow integration."""
import json,sys
def review(d):
 if not isinstance(d,dict) or not isinstance(d.get('tickets'),list) or not d['tickets']:raise ValueError('tickets must be a nonempty list')
 seen=set();out=[]
 for t in d['tickets']:
  if not isinstance(t,dict):raise ValueError('ticket must be an object')
  key=t.get('id')
  if not isinstance(key,str) or not key.strip() or key in seen:raise ValueError('unique nonempty id required')
  seen.add(key)
  for k in ('impact','urgency'):
   if type(t.get(k)) is not int or t[k] not in (1,2,3):raise ValueError(k+' must be integer 1,2,3')
  if t.get('state') not in ('open','resolved'):raise ValueError('state must be open or resolved')
  for k in ('owner','next_update','resolution','verification'):
   if not isinstance(t.get(k),str):raise ValueError(k+' must be a string, empty if unknown')
  if t.get('user_confirmed') not in (True,False,None) or (t.get('user_confirmed') is not None and type(t['user_confirmed']) is not bool):raise ValueError('user_confirmed must be boolean or null')
  gaps=[k for k in ('owner','next_update') if not t[k].strip()]
  if t['state']=='resolved':
   gaps += [k for k in ('resolution','verification') if not t[k].strip()]
   if t.get('user_confirmed') is not True:gaps.append('user_confirmation_pending')
  matrix=((1,2,3),(2,3,4),(3,4,5))
  out.append(dict(id=key,illustrative_priority=matrix[t['impact']-1][t['urgency']-1],review_items=gaps,status='review' if gaps else 'documented_for_review'))
 return {'tickets':out,'limits':'Illustrative priority matrix only. No SLA clock, user authentication, native update or automatic closure. Human applies actual policy.'}
if __name__=='__main__':
 try:
  with open(sys.argv[1],encoding='utf-8') as f:data=json.load(f)
  print(json.dumps(review(data),indent=2))
 except (ValueError,TypeError,KeyError,IndexError,OSError) as e:print('Input error: '+str(e),file=sys.stderr);sys.exit(2)
