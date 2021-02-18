import re
from flask import Flask, request
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Blueprint, render_template, redirect, url_for, request, flash

import datetime
import math

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://exceed_group09:fvgwpw72@158.108.182.0:2255/exceed_group09'
app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
mongo = PyMongo(app)
myTemp = mongo.db.temp
myUser = mongo.db.user
mySn = mongo.db.serial_number

# render is not allowed
# @app.route('/')
# def index():
#     return render_template('index.html')

# render is not allowed
# @app.route('/login')
# def login():
#     return render_template('login.html')


@app.route('/login_post', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')

    flit = {'email' : email}
    data = myUser.find_one(flit)
    if not data:
        # flash('Please check your login details and try again.')
        # return redirect(url_for('login'))
        return {"result" : "check your login details and try again"}
    if not check_password_hash(data["password"],password):
        # flash("Wrong password!!!!!!")
        # return redirect(url_for('login'))
        return {"result" : "Wrong password"}
    # sn = data["sn"]
    # return redirect(url_for("info", sn=sn))
    return {"result" : "login sucessfully"}
    

# @app.route('/info')
# def info():
#     sn = request.args.get('sn')
#     flit = {'sn' : sn}
#     data = myUser.find_one(flit)
#     data_temp = myTemp.find_one(flit)
#     return render_template('info.html', sn=sn, data=data, data_temp=data_temp)

@app.route('/get_info',methods = ["GET"])
def get_info():
    sn = request.args.get('sn')
    flit = {'sn' : sn}
    data = myUser.find_one(flit)
    data_temp = myTemp.find_one(flit)
    # return render_template('info.html', sn=sn, data=data, data_temp=data_temp)
    return {
        "sn" : sn,
        "info" : data,
        "temp" : data_temp
    }

# render is not allowed
# @app.route('/graph')
# def graph():
#     return render_template('graph.html', name='nameeee')


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


@app.route('/convert_avg', methods=["PUT"])
def convert_avg():
    data = request.json
    sn = data['sn']
    all_temp = 0
    all_hr = 0

    daily = myTemp.find_one({'sn': sn})
    d = datetime.datetime.now().day
    m = datetime.datetime.now().month
    tim = str(d)+"-"+str(m)

    for ele in daily['daily_temp']:
        all_temp += ele['temp']
        all_hr += 1

    avg = 0 if all_hr==0 else all_temp/all_hr
    if len(daily['daily_avg']) == 14:
        daily['daily_avg'].pop(0)
    daily['daily_avg'].append({"temp_avg": avg, "day_month": tim})
    daily['daily_temp'] = []
    myTemp.replace_one(
        myTemp.find_one({'sn': sn}),
        daily
    )
    return {"all_temp": all_temp, "all_hr": all_hr, "avg": avg}


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

# render is not allowed
# @app.route('/signup')
# def signup():
#     return render_template('signup.html')


@app.route('/signup_post', methods=['POST'])
def signup_post():
    sn = request.form.get('sn')
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    blood_type = request.form.get('blood-type')
    job = request.form.get('job')

    dataSN = mySn.find_one({'sn': sn})
    
    if not dataSN:
        flash('This serial number is not exist!')
        return redirect(url_for('signup'))
    if dataSN['signed_up']:
        flash('This serial number is already signed up!')
        return redirect(url_for('login'))

    dataEmail = myUser.find_one({'email' : email})

    if dataEmail:
        flash('This email is already signed up!')
        return redirect(url_for('sign_up'))

    data = {
        "sn": sn,
        "email": email,
        "name": name,
        "password": generate_password_hash(password, method='sha256'),
        "blood_type": blood_type,
        "job": job
    }

    myUser.insert_one(data)

    return redirect(url_for('login'))

@app.route('/get_temp', methods=['GET'])
def get_temp():
    data = request.json
    sn = data['sn']
    temp = myTemp.find_one({'sn': sn})
    return temp

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='3000', debug=True)