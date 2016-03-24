#! /usr/bin/env python 

from flask import Flask

app = Flask(__name__)

@app.route("/<name>")
def hello_world(name):
	return "<b>hello %s you are the best boy!</b>" % name

if __name__ == "__main__":
	app.run("0.0.0.0")
