import json

class Player:
    def __init__(self, name, *args):
        self.name = name
        self.dm = True
        if len(args) > 0:
            self.dm = False
            self.charname, self.race, self.class_ = args
    def toJSON(self):
        d = { "name" : self.name, "isDM" : self.dm }
        if not self.dm:
            d["charname"] = self.charname
            d["race"] = self.race
            d["class"] = self.class_
        return json.dumps(d)


