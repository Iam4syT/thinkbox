import json, sys, re
def search(cards, query):
    if not isinstance(query,str) or not query.strip():raise ValueError("query required")
    if not isinstance(cards,list) or not cards:raise ValueError("nonempty card list required")
    seen=set()
    for c in cards:
        if not isinstance(c,dict) or set(c)!={"id","title","steps"}:raise ValueError("exact card schema required")
        if any(not isinstance(c[k],str) or not c[k].strip() for k in c):raise ValueError("card fields must be nonempty text")
        if c["id"] in seen:raise ValueError("duplicate id")
        seen.add(c["id"])
    words=set(re.findall(r"[a-z0-9]+",query.lower()))
    if words & {"password","admin","credential","credentials"}:return "ESCALATE: use approved IT route"
    matched=[c for c in cards if words & set(re.findall(r"[a-z0-9]+",(c["title"]+" "+c["steps"]).lower()))]
    return "\n".join(f"[{c['id']}] {c['title']}: {c['steps']}" for c in matched) or "NO MATCH: ask IT"
if __name__ == "__main__":
    try:
        if len(sys.argv)<3:raise ValueError("usage: search.py cards.json query")
        print(search(json.load(open(sys.argv[1],encoding="utf-8"))," ".join(sys.argv[2:])))
    except (ValueError,OSError) as error:
        print("INVALID:",error);sys.exit(2)
