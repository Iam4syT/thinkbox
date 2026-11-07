"""A local approval state machine with injected Graph-like responses; no API calls."""
import argparse, json, math
class Workflow:
    def __init__(self):self.states={};self.audit=[]
    def submit(self,key,requester,approver):
        if not key or not requester or not approver:raise ValueError('Required field missing')
        if requester==approver:raise ValueError('Self-approval prohibited')
        if key in self.states:return self.states[key]
        self.states[key]={'requester':requester,'approver':approver,'status':'pending','attempts':0}
        self.audit.append({'key':key,'event':'submitted'});return self.states[key]
    def decide(self,key,actor,approve):
        r=self.states[key]
        if actor!=r['approver']:raise PermissionError('Assigned approver required')
        if r['status']!='pending':raise ValueError('Decision already recorded')
        r['status']='approved' if approve else 'rejected'
        self.audit.append({'key':key,'event':r['status']})
    def dispatch(self,key,code=200,retry_after=None):
        r=self.states[key]
        if r['status']=='complete':return {'status':'complete','replayed':True}
        if r['status'] not in {'approved','retry'}:raise PermissionError('Approval required')
        if r['attempts']>=3:r['status']='failed';return {'status':'failed'}
        r['attempts']+=1
        if code==200:r['status']='complete';result={'status':'complete','replayed':False}
        elif code==429:
            try:delay=float(retry_after) if retry_after is not None else 2**r['attempts']
            except (TypeError,ValueError):delay=2**r['attempts']
            if not math.isfinite(delay) or delay<0:delay=2**r['attempts']
            r['status']='retry';result={'status':'retry','retry_after_seconds':delay}
        elif code in {401,403}:r['status']='blocked';result={'status':'blocked'}
        else:r['status']='failed';result={'status':'failed'}
        self.audit.append({'key':key,'event':r['status'],'response_code':code})
        return result
def main():
    a=argparse.ArgumentParser();a.add_argument('--status-code',type=int,default=200);x=a.parse_args()
    w=Workflow();w.submit('demo-1','requester','reviewer');w.decide('demo-1','reviewer',True)
    print(json.dumps({'result':w.dispatch('demo-1',x.status_code,5),'audit':w.audit},indent=2))
if __name__=='__main__':main()
