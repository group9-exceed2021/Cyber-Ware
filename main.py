from flask import Flask, request
from flask_pymongo import PyMongo
from flask import render_template
import datetime
import math

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://exceed_user:1q2w3e4r@158.108.182.0:2277/exceed_backend'
mongo = PyMongo(app)
myCollection = mongo.db.g9

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/graph')
def graph():
    return render_template('graph.html', name='nameeee')

# @app.route()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='3000', debug=True)