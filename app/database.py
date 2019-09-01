import sqlite3

conn = sqlite3.connect('database.db')
print "Executed successfully";

conn.execute('CREATE TABLE members (login_id TEXT, password TEXT)')
print "Table Created successfully";
conn.close()