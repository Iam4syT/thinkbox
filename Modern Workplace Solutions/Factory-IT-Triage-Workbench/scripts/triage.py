"""Decision aid for synthetic tickets. Never connects to devices or machinery."""
import argparse,json
from pathlib import Path
def classify(t):
    evidence=[k for k in ('site','asset_id','symptom','impact','started','checks') if not t.get(k)]
    base={'id':t.get('id'),'missing_fields':evidence,'action':'human-review','priority':'normal','route':'service-desk','boundary':'approved-first-line-checks-only'}
    if t.get('security_suspected') is True:
        boundary='report-follow-incident-procedure'
        if t.get('zone')=='production' or t.get('asset_type') in ('machine-pc','plc','hmi'):
            boundary+='-observe-only-no-reboot-patch-scan-or-plc-change'
        base.update(priority='urgent',route='security-and-service-manager',boundary=boundary)
    elif t.get('zone')=='production' or t.get('asset_type') in ('machine-pc','plc','hmi'):
        base.update(priority='urgent' if t.get('production_stopped') is True else 'review',route='senior-engineer-and-production-owner',boundary='observe-only-no-reboot-patch-scan-or-plc-change')
    elif t.get('asset_type') in ('mac','ipad','iphone'):
        base.update(route='mdm-specialist',boundary='confirm-enrollment-no-wipe')
    elif t.get('symptom_type')=='network':
        base.update(route='first-line-network-check',boundary='check-approved-office-cable-wifi-ip-dns-no-vlan-change')
    elif t.get('symptom_type') in ('account','email','printer'):
        base.update(route='service-desk')
    else:base.update(route='clarify-with-service-manager')
    if evidence and base['priority']=='normal':base['priority']='review'
    return base
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--input',required=True);p.add_argument('--output',required=True);args=p.parse_args()
    data=json.loads(Path(args.input).read_text())
    if not isinstance(data,list):raise ValueError('Input must be a list')
    output=[classify(t) for t in data];Path(args.output).parent.mkdir(parents=True,exist_ok=True);Path(args.output).write_text(json.dumps(output,indent=2)+'\n');print(json.dumps(output,indent=2))
