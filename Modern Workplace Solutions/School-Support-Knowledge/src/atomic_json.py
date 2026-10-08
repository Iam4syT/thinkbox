"""Write a validated local result without replacing the last good file on failure."""
import json, os, tempfile
from pathlib import Path
def write_atomic(path,data):
    path=Path(path); path.parent.mkdir(parents=True,exist_ok=True)
    fd,tmp=tempfile.mkstemp(dir=path.parent,prefix='.queue-')
    try:
        with os.fdopen(fd,'w') as f: json.dump(data,f,indent=2); f.write('\n')
        os.replace(tmp,path)
    finally:
        if os.path.exists(tmp): os.unlink(tmp)
