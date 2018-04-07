#!/usr/bin/env python3
import json
d = None
with open("spells.json", 'r') as f:
    d = json.loads(f.read())
    for k in d:
        print(k)
    exit(1)
    for k in d:
        d[k]["classes"] = []
    with open("spell_classes.txt", "r") as f2:
        curtype = ""
        for line in f2:
            if line[0] == '\t':
                curtype = line.strip()
            else:
                d[line.strip()]["classes"].append(curtype.strip())

