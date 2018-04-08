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
    print(db)
    if request.method == 'GET':
        return render_template('index.html')

    if request.form["charName"]:
        try:
            db.save_player(request.form["roomif"], request.form["name"], request.form["charname"], request.form["class"], request.form["class"])
        except KeyError:
            return redirect(url_for('error'))
        return redirect(url_for('room', name=request.form["charName"], roomid="temp"))

    name = request.form["name"]
    roomid = db.new_game(name)
    return redirect(url_for('room', name=name, roomid=roomid))

@app.route('/<path:filename>')
def serve_static(filename):
    root_dir = os.path.dirname(os.getcwd())
    return send_from_directory(os.path.join(root_dir,'YADCA' ,'static'), filename)

@app.route('/<roomid>/<name>')
def room(roomid, name):
    return render_template("board.html", name=name)

@app.route('/error')
def error():
    return render_template("error.html")

@app.route('/spells')
def spells():
    root_dir = os.path.dirname(os.getcwd())
    return send_from_directory(os.path.join(root_dir,'YADCA' ,'resources'), 'spells_processed.json')

