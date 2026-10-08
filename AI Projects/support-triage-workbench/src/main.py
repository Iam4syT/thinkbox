"""Rules baseline and simulated AI suggestion guard. No external model call."""
import json,argparse
from pathlib import Path
KB={'auth':'KB-auth','rate':'KB-rate','incident':'KB-incident','unknown':None}
def triage(ticket,suggestion=None):
    if not isinstance(ticket.get('text'),str) or not ticket.get('id'): raise ValueError('ticket id/text required')
    s=ticket['text'].lower()
    route='incident' if any(x in s for x in ('outage','all users','5xx')) else 'auth' if any(x in s for x in ('401','login','unauthorized')) else 'rate' if any(x in s for x in ('429','rate limit')) else 'unknown'
    result={'id':ticket['id'],'route':route,'citation':KB[route],'human_review':True,'external_actions':False,'ai_status':'not used'}
    if suggestion is not None:
        valid=isinstance(suggestion,dict) and suggestion.get('route')==route and suggestion.get('citation')==KB[route] and route!='unknown' and suggestion.get('action')=='draft_only'
        result['ai_status']='simulated suggestion accepted for review' if valid else 'simulated suggestion rejected; rules fallback'
    result['handoff']={'owner':'unassigned human','next_check':'verify scope, impact and request IDs; then assign an owner','status':'draft only; do not claim resolution'}
    return result
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--input',default='data/tickets.json');ap.add_argument('--suggestions');a=ap.parse_args()
    suggestions=json.loads(Path(a.suggestions).read_text()) if a.suggestions else {}
    print(json.dumps([triage(t,suggestions.get(t['id'])) for t in json.loads(Path(a.input).read_text())],indent=2))
