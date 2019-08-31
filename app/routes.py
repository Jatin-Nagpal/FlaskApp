from flask import Flask, render_template, url_for, redirect, request
app = Flask(__name__)
log = 0
Name = "Pta Nhi"

@app.route('/')
def home():
	if log is 0:
		return render_template('login.html')
	else:
		return 'Hello %s!' % name

@app.route('/success/<name>/')
def success(name):
	return 'welcome %s' % name

@app.route('/login/',methods = ['POST','GET'])
def login():
	global log
	if log is 0:
		return redirect(url_for('home'))
	elif request.method == 'POST':
		Name = request.form['nm']
		log = 1
		return redirect(url_for('success',name = Name))
	else:
		Name = request.args.get('nm')
		log = 1
		return redirect(url_for('success',name = Name))

@app.route('/hello/<name>/')
def hello(name):
	return 'Hello %s!' % name

if __name__ == '__main__':
	app.run(debug=True)