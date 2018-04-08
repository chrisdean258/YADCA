from Player import Player

class Game:
    def __init__(self, dm_name):
        self.dm = Player(dm_name)
        self.players = []
    def addPlayer(self, name, charname, charrace, charclass):
        self.players.append(Player(name, charname, charrace, charclass))
