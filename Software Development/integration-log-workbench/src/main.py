"""Offline integration diagnosis. No network or customer system access."""
import json, sqlite3, argparse
from pathlib import Path
def diagnose(rows,tenant):
    db=sqlite3.connect(':memory:')
    db.execute('CREATE TABLE logs(tenant TEXT, request_id TEXT, status INTEGER, accepted INTEGER)')
    seen=set()
    for r in rows:
        key=(r['tenant'],r['request_id'])
        if key in seen: continue
        seen.add(key)
        if type(r['status']) is not int or type(r['accepted']) is not int or r['accepted'] not in (0,1):
            raise ValueError('invalid status/acceptance field')
        db.execute('INSERT INTO logs VALUES(?,?,?,?)',(r['tenant'],r['request_id'],r['status'],r['accepted']))
    counts=dict(db.execute('SELECT status,COUNT(*) FROM logs WHERE tenant=? GROUP BY status',(tenant,)).fetchall())
    gap=db.execute('SELECT COUNT(*) FROM logs WHERE tenant=? AND status=200 AND accepted=0',(tenant,)).fetchone()[0]
    findings=[]
    if counts.get(401): findings.append('Authentication refused: check permitted credentials, not a blind retry.')
    if counts.get(429): findings.append('Throttled: inspect Retry-After; retry with a bounded backoff.')
    if sum(v for k,v in counts.items() if 500<=k<=599): findings.append('Server error: record request ID and time, then escalate if persistent.')
    if gap: findings.append('HTTP success but downstream acceptance unknown: inspect ingestion evidence.')
    if not counts: findings.append('No data: distinguish missing logs from no traffic.')
    db.close()
    return {'tenant':tenant,'counts':counts,'unaccepted_success':gap,'findings':findings,'scope':'synthetic offline fixture; not a live integration'}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--input',default='data/logs.json');ap.add_argument('--tenant',default='demo-a');a=ap.parse_args()
    print(json.dumps(diagnose(json.loads(Path(a.input).read_text()),a.tenant),indent=2))
