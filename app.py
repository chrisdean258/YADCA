from flask import Flask
from flask import send_file
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect
from flask import send_from_directory
import Player
import Game
import db
import os

app=Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    if "charName" in request.form and request.form["charName"].strip() != "":
        db.save_player(request.form["roomCode"], request.form["name"], request.form["charName"], request.form["infoClass"], request.form["infoRace"])
        return redirect(url_for('room', name=request.form["charName"], roomid=request.form["roomCode"]))

    name = request.form["name"]
    roomid = db.new_game(name)
    return redirect(url_for('room', name=name, roomid=roomid))

@app.route('/<path:filename>')
def serve_static(filename):
    root_dir = os.path.dirname(os.getcwd())
    return send_from_directory(os.path.join(root_dir,'YADCA' ,'static'), filename)

@app.route('/<roomid>/<name>')
def room(roomid, name):
    return render_template("board.html", name=name, roomid=roomid)

@app.route('/error')
def error():
    return render_template("error.html")

@app.route('/spells')
def spells():
    root_dir = os.path.dirname(os.getcwd())
    return send_from_directory(os.path.join(root_dir,'YADCA' ,'resources'), 'spells_processed.json')

@app.route('/<roomid>/<name>/update', methods=['GET'])
def update(roomid, name):
    game = db.get_game(roomid).getJSONUpdate()
    return game


