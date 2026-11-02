"""Fail-closed review of synthetic model evidence; no deployment action."""
import argparse,json,math,hashlib
from pathlib import Path
REQUIRED={'schema_version','model_id','model_mae_ms','baseline_mae_ms','test_n','data_scope','privacy_review','rollback_plan'}
def review(record):
    if set(record)!=REQUIRED:raise ValueError('schema mismatch')
    if type(record['schema_version']) is not int or record['schema_version']!=1:raise ValueError('unsupported schema')
    if not isinstance(record['model_id'],str) or not record['model_id'] or len(record['model_id'])>80:raise ValueError('invalid model id')
    for k in ['model_mae_ms','baseline_mae_ms']:
        if type(record[k]) not in (int,float) or not math.isfinite(record[k]) or record[k]<0:raise ValueError('invalid metric')
    if type(record['test_n']) is not int or record['test_n']<1:raise ValueError('invalid test size')
    if any(type(record[k]) is not bool for k in ['privacy_review','rollback_plan']):raise ValueError('review flags must be boolean')
    if not isinstance(record['data_scope'],str):raise ValueError('invalid scope')
    reasons=[]
    if record['model_mae_ms']>=record['baseline_mae_ms']:reasons.append('does_not_beat_baseline')
    if record['model_mae_ms']>3:reasons.append('absolute_error_limit')
    if record['test_n']<8:reasons.append('small_test_set')
    if record['data_scope']!='synthetic':reasons.append('data_scope_not_permitted')
    if not record['privacy_review']:reasons.append('privacy_review_missing')
    if not record['rollback_plan']:reasons.append('rollback_plan_missing')
    digest=hashlib.sha256(json.dumps(record,sort_keys=True,allow_nan=False).encode()).hexdigest()
    return {'model_id':record['model_id'],'decision':'hold' if reasons else 'await_human_review','reasons':reasons,'input_sha256':digest,'deployment_performed':False}
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('input',nargs='?',default=str(Path(__file__).parent/'data/example.json'));a=p.parse_args()
    print(json.dumps(review(json.loads(Path(a.input).read_text())),indent=2))
