class Player:
    def __init__(self, name, *args):
        self.name = name
        self.dm = True
        if len(args) > 0:
            self.dm = False
            self.charname, self.race, self.class_


