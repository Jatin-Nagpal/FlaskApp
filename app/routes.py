from flask import Flask, render_template, url_for, redirect, request
import sys, socket, selectors, traceback

app = Flask(__name__)

@app.route('/success/<name>/')
def success(name):
	return 'welcome %s' % name

@app.route('/login/',methods = ['POST','GET'])
def login():
	if request.method == 'POST':
		user = request.form['nm']
		return redirect(url_for('success',name = user))
	else:
		user = request.args.get('nm')
		return redirect(url_for('success',name = user))


@app.route('/')
def home():
	return render_template('login.html')
	# return redirect(url_for('login'))

@app.route('/hello/<name>/')
def hello(name):
	return 'Hello %s!' % name

if __name__ == '__main__':
	app.run(debug=True)