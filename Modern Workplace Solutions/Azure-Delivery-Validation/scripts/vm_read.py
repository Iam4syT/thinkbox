"""Unrun Azure VM read exercise. Review and run only inside the scoped VM."""
import json,hashlib,sys
from urllib.request import Request,urlopen
from urllib.error import HTTPError,URLError
from urllib.parse import urlsplit,urlencode

def main():
 if len(sys.argv)!=2: print("Supply the scoped HTTPS blob URL");return 2
 u=urlsplit(sys.argv[1])
 if u.scheme!="https" or not u.hostname or not u.hostname.endswith(".blob.core.windows.net") or u.query or u.username or u.password:
  print("Only a scoped Azure blob HTTPS URL, without credentials or query, is accepted");return 2
 try:
  params=urlencode({"api-version":"2018-02-01","resource":"https://storage.azure.com/"})
  request=Request("http://169.254.169.254/metadata/identity/oauth2/token?"+params,headers={"Metadata":"true"})
  with urlopen(request,timeout=10) as response: token=json.load(response)["access_token"]
  request=Request(sys.argv[1],headers={"Authorization":"Bearer "+token,"x-ms-version":"2023-11-03"})
  with urlopen(request,timeout=15) as response:
   content=response.read(1048577)
   if len(content)>1048576: print("Expected a small synthetic blob");return 2
   print(json.dumps({"http_status":response.status,"sha256":hashlib.sha256(content).hexdigest(),"bytes":len(content)}))
  return 0
 except HTTPError as error: print(json.dumps({"status":"HTTP_FAILURE","code":error.code}));return 1
 except (URLError,KeyError,ValueError): print(json.dumps({"status":"READ_FAILURE"}));return 1
if __name__=="__main__":sys.exit(main())
