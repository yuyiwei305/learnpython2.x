#! /usr/bin/env python

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return "it is index !!!"

@app.route("/sum/<int:a>/<int:b>")
def sum(a,b):
	return " %d + %d = %d" % (a,b,a+b)


if __name__ == "__main__":
	app.run(host="0.0.0.0")
