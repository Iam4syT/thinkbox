"""Offline retrieval baseline: synthetic ACL metadata, no cloud or model call."""
import argparse,json,re
from pathlib import Path
GROUPS={"reader-a":{"public","matter-a"},"reader-b":{"public","matter-b"},"visitor":{"public"}}
def words(text): return set(re.findall(r"[a-z0-9]+",text.lower()))
def search(documents,role,query):
    if role not in GROUPS: raise ValueError("Unknown role")
    if not isinstance(query,str) or not query.strip() or len(query)>1000: raise ValueError("Invalid query")
    if not isinstance(documents,list): raise ValueError("Documents must be a list")
    ids=set(); hits=[]
    for doc in documents:
        if not isinstance(doc,dict) or set(doc)-{"id","source","text","groups"}: raise ValueError("Invalid document fields")
        if not all(isinstance(doc.get(k),str) and doc[k].strip() for k in ["id","source","text"]): raise ValueError("Invalid document")
        if doc["id"] in ids: raise ValueError("Duplicate id")
        ids.add(doc["id"])
        groups=doc.get("groups")
        if groups is None or groups==[]: continue
        if not isinstance(groups,list) or any(not isinstance(g,str) for g in groups): raise ValueError("Invalid groups")
        if not GROUPS[role].intersection(groups): continue
        # Filter first; every chunk inherits its parent ACL and citation.
        paragraphs=[p for p in doc["text"].split("\n\n") if p.strip()]
        for number,p in enumerate(paragraphs,1):
            score=len(words(query)&words(p))
            if score: hits.append(dict(id=doc["id"],chunk=number,source=doc["source"],quote=p,score=score))
    hits.sort(key=lambda h:(-h["score"],h["id"],h["chunk"]))
    return {"status":"REVIEW_SOURCES" if hits else "ABSTAIN","results":hits[:3]}
if __name__=="__main__":
    a=argparse.ArgumentParser();a.add_argument("--role",default="visitor");a.add_argument("--query",default="retention");a.add_argument("--data",default="data/documents.json");x=a.parse_args()
    try: print(json.dumps(search(json.loads(Path(x.data).read_text()),x.role,x.query),indent=2))
    except (ValueError,OSError) as e: raise SystemExit("INVALID INPUT: "+str(e))
