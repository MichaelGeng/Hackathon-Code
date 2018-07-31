import sqlite3
import json
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/api/users')
def get_users():
    customers = ["Michael", "Harvir", "Colby", "Meg"]

    return json.dumps(customers)

@app.route('/api/userdb_create')
def user_query():

    conn = sqlite3.connect('tutorial.db')
    c = conn.cursor()

    c.execute('CREATE TABLE IF NOT EXISTS user_info (email TEXT, name TEXT, username TEXT, password TEXT)')
    c.execute("INSERT INTO user_info VALUES ('mikegeng@umich.edu', 'Michael Geng', 'mikegeng', '1234')")
    c.execute("INSERT INTO user_info VALUES ('harvir@gmail.com', 'Harvir Chima', 'mikegeng', '1234')")
    c.execute("INSERT INTO user_info VALUES ('ctriolo@gmail.com', 'Colby Triolo', 'cboly', '1234')")

    conn.commit()
    c.close()
    conn.close()

    return 'All good'
