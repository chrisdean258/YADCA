import json
from Player import Player

class Game:
    def __init__(self, dm_name):
        self.players = [Player(dm_name)]
    def addPlayer(self, name, charname, charrace, charclass):
        self.players.append(Player(name, charname, charrace, charclass))
    def getPlayer(self, name):
        return list(filter(lambda player: player.searchname== name, self.players))[0]
    def getDM(self):
        return self.dm
    def getJSONUpdate(self, name):
        d = {}
        player = self.getPlayer(name)
        d["players"] = [json.loads(p.toJSON()) for p in self.players]
        d["messages"] = [p[0] for p in player.messages]
        d["messages_from"] = [p[1] for p in player.messages]
        d["messages_to"] = [p[2] for p in player.messages]
        d["dm"] = player.dm
        player.messages = []
        return json.dumps(d)
