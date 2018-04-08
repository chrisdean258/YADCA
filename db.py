from Game import Game
db = {}

def save_player(roomid, playername, charname, charclass, charrace):
    global db
    db[str(roomid)].addPlayer(playername, charname, charclass, charrace)

def new_game(dm_name):
    global db
    roomid = len(db)
    while str(roomid) in db:
        roomid += 1
    db[str(roomid)] = Game(dm_name)
    return roomid

def get_game(roomid):
    return db[str(roomid)]


