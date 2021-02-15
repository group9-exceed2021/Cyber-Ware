from flask import Flask, request
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Blueprint, render_template, redirect, url_for, request, flash

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

@app.route('/new_temp', methods=['POST'])
def new_temp():
    data = request.json
    sn = data['sn']
    # data ขึ้น mongo

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signup_post', methods=['POST'])
def signup_post():
    sn = request.form.get('sn')
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    # if sn not in db:
    #     flash('No sn')
    #     return redirect(url_for('signup'))

    # if sn already exist:
    #     flash('Email address already exists')
    #     return redirect(url_for('signup'))

    # if sn not in db:
    #     return redirect(url_for('signup'))

    data = {
        "sn": sn,
        "email": email,
        "name": name,
        "password": generate_password_hash(password, method='sha256')
    }

    myCollection.insert_one(data)
    # return login
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='3000', debug=True)