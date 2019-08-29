from flask import Flask, render_template, url_for, redirect
import sys
import socket
import selectors
import traceback
import libserver

app = Flask(__name__)

@app.route('/')
def home():
	return 'Hello World'

@app.route('/hello/<name>/')
def hello(name):
	return 'Hello %s!' % name

if __name__ == '__main__':
	app.run(debug=True)