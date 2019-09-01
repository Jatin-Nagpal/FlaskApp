from flask import Flask, session, render_template, url_for, redirect, request, escape
app=Flask(__name__)
app.secret_key = 'any random string'

@app.route('/')
def home():
	if 'handle' in session:
		handle = session['handle']
		return 'Logged in as ' + handle + '<br>' +\
		"<b><a href = '/logout'>Click here to log out</a></b>"
	return redirect(url_for('login'))

@app.route('/login/')
def login():
	return render_template('login.html')

@app.route('/loggedin/',methods = ['POST','GET'])
def loggedin():
	if request.method == 'POST':
		session['handle'] = request.form['handle']
		return redirect(url_for('home'))

@app.route('/logout')
def logout():
	session.pop('handle', None)
	return redirect(url_for('home'))

@app.route('/regis',methods = ['POST','GET'])
def regis():
	return redirect(url_for('register'))

@app.route('/register',methods = ['POST','GET'])
def register():
	return



if __name__ == '__main__':
	app.run(debug=True)