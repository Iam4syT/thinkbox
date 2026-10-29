"""Synthetic discovery worksheet. Illustrative economics, not a licence quote."""
import json, math, sys

def number(data,key,positive=False):
    v=data.get(key)
    if isinstance(v,bool) or not isinstance(v,(int,float)) or not math.isfinite(v) or v<0 or (positive and v==0):
        raise ValueError(key+' must be a finite '+('positive' if positive else 'non-negative')+' number')
    return v

def plan(d):
    seats=number(d,'seats',True)
    if int(seats)!=seats: raise ValueError('seats must be a whole number')
    mins=number(d,'minutes_per_week'); rate=number(d,'hourly_value'); monthly=number(d,'monthly_licence'); setup=number(d,'setup_cost')
    if d.get('workflow') not in ('collaboration','email'): raise ValueError('workflow must be collaboration or email')
    readiness=d.get('readiness')
    if readiness not in ('reviewed','unknown','risk'): raise ValueError('readiness must be reviewed, unknown or risk')
    gross=seats*mins/60*52*rate
    cost=seats*monthly*12+setup
    return {'decision':'pilot_candidate' if readiness=='reviewed' else 'review_first',
      'option':'Teams and SharePoint workflow' if d['workflow']=='collaboration' else 'Exchange recipient options review',
      'illustrative_annual_capacity_value':round(gross,2),'illustrative_first_year_cost':round(cost,2),
      'illustrative_net_value':round(gross-cost,2),
      'assumptions':'All prices and time benefits are fictional inputs. Capacity value is not cash savings or achieved ROI.',
      'next_step':'Validate user need, permissions, licence entitlement, pilot quality and baseline with customer; human approves.'}

if __name__=='__main__':
    try:
        with open(sys.argv[1],encoding='utf-8') as f: data=json.load(f)
        print(json.dumps(plan(data),indent=2))
    except (ValueError,KeyError,IndexError,OSError,TypeError) as e:
        print('Input error: '+str(e),file=sys.stderr);sys.exit(2)
