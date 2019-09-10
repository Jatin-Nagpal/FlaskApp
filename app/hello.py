from flask import Flask, session, render_template, url_for, redirect, request, escape
app=Flask(__name__)
from flask_bootstrap import Bootstrap
import sqlite3 as sql
app.secret_key = 'any random string'

def create_app():
	app = Flask(__name__)
	Bootstrap(app)
	return app

posts = [
	{
		'author': 'Jatin Nagpal',
		'title': 'First Blog',
		'content': 'First post content',
		'date_posted': 'September 10, 2019'
	}
]

@app.route('/home/')
@app.route('/')
def home():
	if 'handle' in session:
		handle = session['handle']
		return render_template('home.html', posts=posts,title = 'Home Page')
		# return 'Logged in as ' + handle + '<br>' +\
		# "<b><a href = '/logout'>Click here to log out</a></b>"
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
				msg = "Coder Successfully Added"
		except:
			con.rollback()
			msg = "Error in insert operation"

		finally:
			return render_template("result.html", msg = msg)
			con.close()

@app.route('/list/')
def list():
	con = sql.connect("database.db")
	con.row_factory = sql.Row

	cur = con.cursor()
	cur.execute("select * from coders")

	rows = cur.fetchall();
	return render_template("list.html", rows = rows)

@app.route('/register/',methods = ['POST','GET'])
def register():
	return render_template("register.html")

if __name__ == '__main__':
	app.run(debug=True)
