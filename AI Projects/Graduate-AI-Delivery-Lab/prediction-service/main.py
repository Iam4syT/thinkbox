import json,math,argparse
from pathlib import Path
from urllib.parse import parse_qs,urlsplit
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
def load(path):
    data=json.loads(Path(path).read_text())
    if set(data)!={'version','slope','intercept','scope'} or data['version']!='demo-v1' or data['scope']!='synthetic_local_only':raise ValueError('unsupported model')
    for k in ['slope','intercept']:
        if isinstance(data[k],bool) or not isinstance(data[k],(int,float)) or not math.isfinite(data[k]):raise ValueError('invalid coefficients')
    return data
def predict(data,query):
    if set(query)!={'x'} or len(query['x'])!=1:raise ValueError('one x required')
    x=float(query['x'][0])
    if not math.isfinite(x) or not 0<=x<=100:raise ValueError('x outside synthetic range')
    y=data['slope']*x+data['intercept']
    if not math.isfinite(y):raise ValueError('nonfinite output')
    return dict(prediction=y,version=data['version'],scope=data['scope'])
def route(model,path):
    u=urlsplit(path)
    if u.path=='/health' and not u.query:return 200,dict(status='ok',version=model['version'])
    if u.path=='/predict':
        try:return 200,predict(model,parse_qs(u.query,keep_blank_values=True))
        except (ValueError,OverflowError):return 400,dict(error='invalid input')
    return 404,dict(error='not found')
def server(path,port=0):
    model=load(path)
    class Handler(BaseHTTPRequestHandler):
        def log_message(self,*args):pass
        def do_GET(self):
            code,body=route(model,self.path)
            self.server.counts[str(code)]=self.server.counts.get(str(code),0)+1
            payload=json.dumps(body,allow_nan=False).encode();self.send_response(code);self.send_header('Content-Type','application/json');self.send_header('Content-Length',str(len(payload)));self.end_headers();self.wfile.write(payload)
    srv=ThreadingHTTPServer(('127.0.0.1',port),Handler);srv.counts={};return srv
if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('--port',type=int,default=8765);a.add_argument('--model',type=Path,default=Path(__file__).parent/'model/model.json');args=a.parse_args()
    srv=server(args.model,args.port);print('Synthetic loopback demo only; Ctrl-C stops.',flush=True)
    try:srv.serve_forever()
    except KeyboardInterrupt:pass
    finally:srv.server_close();print(json.dumps(dict(request_status_counts=srv.counts)))
