#!/usr/bin/env python3
import json

d = {}

with open("spells.json", "r") as infile:
    d = json.loads(infile.read())

for spell in d:
    fields = [spell["name"],
            "<i>"+spell["type"]+"</i>",
            "<b>Casting Time: </b>" + spell["casting_time"],
            "<b>Range: </b>" + spell["range"],
            "<b>Componets: </b>" + spell["components"]["raw"],
            "<b>Duration: </b>" + spell["range"],
            spell["description"]]
    if "higher_levels" in d:
        fields.append("<b>At Higher Levels.</b>" + spell["higher_levels"])
    spell["html_description"] = "<br>".join(fields)

    fields = [spell["name"], " ".join(spell["tags"]), spell["school"]]
    spell["search_string"] = " ".join(fields)



with open("spells_processed.json", "w") as outfile:
    outfile.write(json.dumps(d))

