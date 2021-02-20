import re
from flask import Flask, request,jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS, cross_origin
import requests
import urllib, json
from os import path, environ
from os.path import join, dirname
# from dotenv import load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Blueprint, render_template, redirect, url_for, request, flash

import datetime, pytz
import math

# dotenv_path = join(dirname(__file__), '.env')
# load_dotenv(dotenv_path)

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://exceed_group09:fvgwpw72@158.108.182.0:2255/exceed_group09'
app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
mongo = PyMongo(app)
myTemp = mongo.db.temp
myUser = mongo.db.user
mySn = mongo.db.serial_number
cors = CORS(app, resources={r"/": {"origins": "*"}})

# render is not allowed
@app.route('/')
@cross_origin()
def index():
    return {"notthing": "not"}


@app.route('/login_post', methods=['POST'])
@cross_origin()
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    flit = {'email' : email}
    data = myUser.find_one(flit)
    if not data:
        return {"result" : "check your login details and try again"}
    if not check_password_hash(data["password"],password):
        return {"result" : "Wrong password"}
    return {"result" : "login successfully"}


@app.route('/get_info',methods = ["GET"])
@cross_origin()
def get_info():
    email = request.args.get('email')
    flit = {'email' : email}
    data = myUser.find_one(flit)
    sn = data["sn"]
    filt2 = {"sn": sn}
    data_temp = myTemp.find_one(filt2)
    # datatest = {
    #     "sn": data['sn'],
    #     "email": data['email'],
    #     "firstname": data['firstname'],
    #     "surname": data['surname'],
    #     "blood_type": data['blood_type'],
    #     "job": data['job']
    # }
    return {
        "sn": data['sn'],
        "email": data['email'],
        "firstname": data['firstname'],
        "surname": data['surname'],
        "blood_type": data['blood_type'],
        "job": data['job'],
        "show_temp" : data_temp["daily_temp"][len(data_temp["daily_temp"])-1]['temp'],
        "daily_temp" : data_temp['daily_temp'],
        "avg": data_temp['daily_avg']
    }
    # return {"fdd": "ghcdg"}

@app.route('/new_temp', methods=['POST'])
@cross_origin()
def new_temp():
    data2 = request.json
    sn = data2['sn']
    temp = data2['temp']

    tz = pytz.timezone('Asia/Bangkok')

    m = datetime.datetime.now(tz).month
    d = datetime.datetime.now(tz).day
    h = datetime.datetime.now(tz).hour

    data = myTemp.find_one({'sn': sn})
    if len(data['daily_temp']) != 0:
        thelast = data['daily_temp'][len(data['daily_temp'])-1]
        if thelast['day'] != d:
            all_temp = 0
            all_hr = 0
            daily = myTemp.find_one({'sn': sn})
            tim = str(thelast["day"])+"-"+str(thelast["month"])
            for ele in daily['daily_temp']:
                all_temp += ele['temp']
                all_hr += 1
            avg = 0 if all_hr==0 else all_temp/all_hr
            print(avg)
            if len(daily['daily_avg']) == 14:
                daily['daily_avg'].pop(0)
            daily['daily_avg'].append({"temp_avg": avg, "day_month": tim})
            daily['daily_temp'] = []
            myTemp.replace_one(
                myTemp.find_one({'sn': sn}),
                daily
            )
    data = myTemp.find_one({'sn': sn})
    data['daily_temp'].append({"temp": temp, "month" : m, "day": d, "hour": h})
    myTemp.replace_one(
        myTemp.find_one({'sn': sn}),
        data
    )
    return {"result": "add new temp done"}


@app.route('/test', methods=['GET'])
@cross_origin()
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
@cross_origin()
def signup_post():
    sn = request.form.get('sn')
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    blood_type = request.form.get('blood-type')
    job = request.form.get('job')

    dataSN = mySn.find_one({'sn': sn})
    
    if not dataSN:
        return {"result" : 'This serial number is not exist!'}
    if dataSN['signed_up']:
        return {"result" : 'This serial number is already signed up!'}

    dataEmail = myUser.find_one({'email' : email})

    if dataEmail:
        return {"result" : 'This email is already signed up!'}

    data = {
        "sn": sn,
        "email": email,
        "name": name,
        "password": generate_password_hash(password, method='sha256'),
        "blood_type": blood_type,
        "job": job
    }

    myUser.insert_one(data)
    myTemp.insert_one({
        "sn": sn,
        "daily_temp": [],
        "daily_avg": []
    })
    return {"result" : "login successful"}

@app.route('/get_th_stat', methods=['GET'])
@cross_origin()
def get_th_stat():
    uri = "https://covid19.th-stat.com/api/open/today"
    try:
        uResponse = requests.get(uri)
    except requests.ConnectionError:
       return "Connection Error"  
    Jresponse = uResponse.json()
    return Jresponse

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='3000', debug=True)