from flask import Flask, session, render_template, url_for, redirect, request, escape
app=Flask(__name__)
import sqlite3 as sql
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

@app.route('/logout/')
def logout():
	session.pop('handle', None)
	return redirect(url_for('home'))

global msg
msg = "Hello"
@app.route('/regis/',methods = ['POST','GET'])
def regis():
	if request.method == 'POST':
		try:
			handle = request.form['handle']
			email = request.form['email']
			password = request.form['password']

			with sql.connect("database.db") as con:
				cur = con.cursor()
				cur.execute("INSERT INTO coders (handle,email,password) VALUES (?,?,?)", (handle,email,password) )
				con.commit()
				global msg
				msg = "Coder Successfully Added"
		except:
			con.rollback()
			global msg
			msg = "Error in insert operation"

		finally:
			global msg
			return render_template("result.html", msg = msg)
			con.close()

@app.route('/list/')
def list():
	con = sql.connect("database.db")
	con.row_factory = sql.Row

	cur = con.cursor()
	cur.execute("select * from students")

	rows = cur.fetchall();
	return render_template("list.html", rows = rows)

@app.route('/register/',methods = ['POST','GET'])
def register():
	return render_template("register.html")



if __name__ == '__main__':
	app.run(debug=True)