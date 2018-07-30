from flask import Flask
import json
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route('/api/users')
def get_users():
    customers = ["Michael", "Harvir", "Colby"]

    return json.dumps(customers)
