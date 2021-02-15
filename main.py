from flask import Flask, request
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Blueprint, render_template, redirect, url_for, request, flash

import datetime
import math

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://exceed_group09:fvgwpw72@158.108.182.0:2255/exceed_group09'
mongo = PyMongo(app)
myTemp = mongo.db.temp
myUser = mongo.db.user

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/graph')
def graph():
    return render_template('graph.html', name='nameeee')

@app.route('/new_temp', methods=['POST'])
def new_temp():
    data2 = request.json
    sn = data2['sn']
    temp = data2['temp']
    h = datetime.datetime.now().hour
    data = myTemp.find_one({'sn': sn})
    data['daily_temp'].append({"temp": temp, "hour": h})
    myTemp.replace_one(
        myTemp.find_one({'sn': sn}),
        data
    )
    return {"result": "add new temp done"}
    # data ขึ้น mongo

@app.route('/convert_avg', methods=["POST"])
def convert_avg():
    data = request.json
    sn = data['sn']
    all_temp = 0
    all_hr = 0
    daily = myTemp.find_one({'sn': sn})
    d = datetime.datetime.now().day
    m = datetime.datetime.now().month
    tim = str(d)+"-"+str(m)
    # print(daily_temp)
    # return "daily_temp"
    for ele in daily['daily_temp']:
        all_temp += ele['temp']
        all_hr += 1
    avg = all_temp/all_hr
    daily['daily_avg'].append({"temp_avg": avg, "day_month": tim})
    daily['daily_temp'] = []
    myTemp.replace_one(
        myTemp.find_one({'sn': sn}),
        daily
    )
    return {"all_temp": all_temp, "all_hr": all_hr, "avg": avg}

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/test', methods=['GET'])
def test():
    data = {
        "sn": "sample sn",
        "email": "sample email",
        "name": "sample name",
        "password": generate_password_hash("sample password", method='sha256')
    }
    myUser.insert_one(data)
    return {"data": "done add test"}

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

    myUser.insert_one(data)
    
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='3000', debug=True)