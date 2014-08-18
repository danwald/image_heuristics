#!/usr/bin/python

import bottle
import os

import bottle
from bottle import template
import os



app = application = bottle.Bottle()

@app.route('/')
def show_index():
        return 'Hello, can i has some images?'

if __name__ == '__main__':
        bottle.run(app=app, host='0.0.0.0', port=8080) ##host='0.0.0.0', which makes visitable outside.
