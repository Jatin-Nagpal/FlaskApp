from flask import Flask, render_template, url_for, redirect, request
app=Flask(__name__)

val=0

@app.route('/')
def home():
	global val
	val=1
	return 'Hello World!'

@app.route('/here/')
def here():
	if val is 1:
		return 'Hello, U reached here'
	else:
		return 'Hello, U were unable to reach here'

if __name__ == '__main__':
	app.run()