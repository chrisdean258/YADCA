from flask import Flask
from flask import send_file
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect
from flask import send_from_directory
import os

app=Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    return redirect(url_for('index'))

@app.route('/<path:filename>')
def serve_static(filename):
    root_dir = os.path.dirname(os.getcwd())
    print(root_dir)
    return send_from_directory(os.path.join(root_dir,'YADCA' ,'static'), filename)

