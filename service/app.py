#!/usr/bin/python

import bottle
from bottle import default_app
import os



app = application = bottle.Bottle()

@app.route('/')
def show_index():
        return 'Hello, can i has some images?'

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=8080, debug=True) ##host='0.0.0.0', which makes visitable outside.
