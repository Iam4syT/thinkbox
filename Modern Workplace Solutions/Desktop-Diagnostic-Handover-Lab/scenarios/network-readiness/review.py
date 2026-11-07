"""Review an offline network snapshot; never alter network settings."""
import ipaddress,json,sys
FIELDS={"device","ipv4","gateway","dns_ok","tcp443_ok","physical_check","patch_review"}
def review(row):
 if not isinstance(row,dict) or set(row)!=FIELDS: raise ValueError("invalid snapshot schema")
 if not isinstance(row["device"],str) or not row["device"].strip(): raise ValueError("device required")
 for k in ["dns_ok","tcp443_ok","physical_check","patch_review"]:
  if row[k] is not None and type(row[k]) is not bool: raise ValueError("checks must be true, false or null")
 findings=[]
 for k in ["ipv4","gateway"]:
  if not isinstance(row[k],str): raise ValueError("IP text required")
  try: addr=ipaddress.IPv4Address(row[k])
  except ipaddress.AddressValueError as e: raise ValueError("invalid IPv4") from e
  if k=="ipv4" and addr.is_link_local: findings.append("link-local address: inspect DHCP and link")
  if addr.is_unspecified: findings.append(k+" missing")
 for k in ["dns_ok","tcp443_ok","physical_check","patch_review"]:
  if row[k] is None: findings.append(k+" not observed")
  elif not row[k]: findings.append(k+" failed: investigate")
 return {"device":row["device"],"status":"needs review" if findings else "recorded checks passed", "findings":findings,"approved_for_deployment":False,"human_review":True}
if __name__=="__main__":
 try: print(json.dumps(review(json.load(open(sys.argv[1],encoding="utf-8"))),indent=2))
 except (ValueError,OSError,IndexError) as e: print(str(e),file=sys.stderr);sys.exit(2)
