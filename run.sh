#!/bin/bash
export FLASK_APP=app.py
export FLASK_DEBUG=1
#export LANG=C.UTF-8
#export LC_ALL=C.UTF-8

flask run --host=0.0.0.0
