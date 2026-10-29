"""Read-only fictional inventory allocation; does not reserve or deploy assets."""
import json,sys
def review(d):
 if not isinstance(d,dict) or not isinstance(d.get('stock'),list) or not d['stock'] or not isinstance(d.get('demand'),dict) or not d['demand']:raise ValueError('nonempty stock list and demand object required')
 totals={};seen=set()
 for r in d['stock']:
  if not isinstance(r,dict):raise ValueError('stock row must be object')
  key=r.get('sku')
  if not isinstance(key,str) or not key.strip() or key in seen:raise ValueError('unique nonempty sku required')
  seen.add(key)
  for k in ('on_hand','reserved','quarantined'):
   if type(r.get(k)) is not int or r[k]<0:raise ValueError(k+' must be nonnegative integer')
  if r['reserved']+r['quarantined']>r['on_hand']:raise ValueError('unavailable quantities exceed on_hand')
  totals[key]=r['on_hand']-r['reserved']-r['quarantined']
 shortages={}
 for sku,q in d['demand'].items():
  if not isinstance(sku,str) or not sku.strip() or type(q) is not int or q<=0:raise ValueError('demand must use nonempty SKU and positive integer')
  lack=max(0,q-totals.get(sku,0))
  if lack:shortages[sku]=lack
 checks=d.get('checks')
 if not isinstance(checks,dict):raise ValueError('checks object required')
 names=('network_test','device_test','licence_review','owner_signoff')
 for k in names:
  if k not in checks or (checks[k] is not None and type(checks[k]) is not bool):raise ValueError(k+' must be boolean or null')
 pending=[k for k in names if checks[k] is not True]
 return {'status':'review_required' if shortages or pending else 'recorded_checks_complete','available':totals,'shortages':shortages,'pending_checks':pending,'limits':'Fictional reported checks only; no stock reservation, purchase, physical test, network change or opening approval.'}
if __name__=='__main__':
 try:
  with open(sys.argv[1],encoding='utf-8') as f:data=json.load(f)
  print(json.dumps(review(data),indent=2))
 except (ValueError,TypeError,KeyError,IndexError,OSError) as e:print('Input error: '+str(e),file=sys.stderr);sys.exit(2)
