"""Validate synthetic, aggregated M365 usage data. No service connections."""
import csv, json, sys
def analyse(rows):
    seen=set(); output=[]
    for r in rows:
        key=(r['cohort'].strip(),r['service'].strip())
        if not all(key) or key in seen: raise ValueError('Missing or duplicate cohort/service')
        seen.add(key)
        try: n,a,pn,pa=[int(r[k]) for k in ['licensed','active','previous_licensed','previous_active']]
        except (ValueError,KeyError): raise ValueError('Counts must be whole numbers')
        if min(n,a,pn,pa)<0 or a>n or pa>pn: raise ValueError('Invalid count or denominator')
        if r['period_days'] != '30': raise ValueError('Use matched 30-day windows')
        item={'cohort':key[0],'service':key[1]}
        if min(n,pn)<5:
            item.update(state='suppressed',reason='Small or zero cohort; no rates or counts exported')
        else:
            rate=round(100*a/n,2);previous=round(100*pa/pn,2)
            item.update(state='review',active_rate_percent=rate,previous_rate_percent=previous,change_percentage_points=round(rate-previous,2),next_action='Check data age, role needs and colleague feedback; no automatic licence action')
        output.append(item)
    if not output: raise ValueError('No records')
    return {'mode':'synthetic offline','window_days':30,'findings':output,'limit':'Usage is not productivity or licence eligibility'}
if __name__=='__main__':
    try:
        with open(sys.argv[1],newline='',encoding='utf-8') as f: result=analyse(list(csv.DictReader(f)))
        print(json.dumps(result,indent=2))
    except (ValueError,KeyError,IndexError,OSError) as exc:
        print('Input rejected: '+str(exc),file=sys.stderr);sys.exit(2)
