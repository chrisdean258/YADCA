from flask import Flask
from flask import send_file
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect

app=Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
