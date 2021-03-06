import datetime
import pytz

import requests
from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://exceed_group09:fvgwpw72@158.108.182.0:2255/exceed_group09'
app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
mongo = PyMongo(app)
myTemp = mongo.db.temp
myUser = mongo.db.user
mySn = mongo.db.serial_number
cors = CORS(app, resources={r"/": {"origins": "*"}})


@app.route('/')
@cross_origin()
def index():
    return {"nothing": "not"}


@app.route('/login_post', methods=['POST'])
@cross_origin()
def login_post():
    datalog = request.json
    flit = {'email': datalog['email']}
    data = myUser.find_one(flit)
    if not data:
        return {"result": "Check your login details and try again."}
    if not check_password_hash(data["password"], datalog['password']):
        return {"result": "Wrong password"}
    return {"result": "login successfully"}


@app.route('/get_info', methods=["GET"])
@cross_origin()
def get_info():
    email = request.args.get('email')
    flit = {'email': email}
    data = myUser.find_one(flit)
    sn = data["sn"]
    filt2 = {"sn": sn}
    data_temp = myTemp.find_one(filt2)
    if len(data_temp["daily_temp"]) == 0:
        show = 'nothing'
    else:
        show = data_temp["daily_temp"][len(data_temp["daily_temp"]) - 1]['temp']
    return {
        "sn": data['sn'],
        "email": data['email'],
        "firstname": data['firstname'],
        "surname": data['surname'],
        "blood_type": data['blood_type'],
        "job": data['job'],
        "show_temp": show,
        "daily_temp": data_temp['daily_temp'],
        "avg": data_temp['daily_avg']
    }


@app.route('/new_temp', methods=['POST'])
@cross_origin()
def new_temp():
    data2 = request.json
    sn = data2['sn']
    temp = data2['temp']

    tz = pytz.timezone('Asia/Bangkok')

    y = datetime.datetime.now(tz).year
    m = datetime.datetime.now(tz).month
    d = datetime.datetime.now(tz).day
    h = datetime.datetime.now(tz).hour
    mi = datetime.datetime.now(tz).minute
    sec = datetime.datetime.now(tz).second

    data = myTemp.find_one({'sn': sn})
    if len(data['daily_temp']) != 0:
        the_last = data['daily_temp'][len(data['daily_temp']) - 1]
        if the_last['day'] != d:
            all_temp = 0
            all_hr = 0
            daily = myTemp.find_one({'sn': sn})
            for ele in daily['daily_temp']:
                all_temp += ele['temp']
                all_hr += 1
            avg = 0 if all_hr == 0 else all_temp / all_hr
            if len(daily['daily_avg']) == 14:
                daily['daily_avg'].pop(0)
            daily['daily_avg'].append(
                {"temp_avg": avg, "year": the_last["year"], "month": the_last["month"], "day": the_last['day']})
            daily['daily_temp'] = []
            myTemp.replace_one(
                myTemp.find_one({'sn': sn}),
                daily
            )
    data = myTemp.find_one({'sn': sn})
    data['daily_temp'].append({"temp": temp, "year": y, "month": m, "day": d, "hour": h, "minute": mi, "sec": sec})
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
    data_json = request.json
    data_sn = mySn.find_one({'sn': data_json['sn']})

    if not data_sn:
        return {"result": 'This serial number is not exist!'}
    if data_sn['signed_up'] == 1:
        return {"result": 'This serial number is already signed up!'}

    data_email = myUser.find_one({'email': data_json['email']})

    if data_email:
        return {"result": 'This email is already signed up!'}

    data = {
        "sn": data_json['sn'],
        "email": data_json['email'],
        "firstname": data_json['firstname'],
        "surname": data_json["surname"],
        "password": generate_password_hash(data_json['password'], method='sha256'),
        "blood_type": data_json['bloodType'],
        "job": data_json['job']
    }

    update = {"$set": {"signed_up": 1}}
    mySn.update_one({'sn': data_json['sn']}, update)

    myUser.insert_one(data)
    myTemp.insert_one({
        "sn": data_json["sn"],
        "daily_temp": [],
        "daily_avg": []
    })
    return {"result": "signup successful"}


@app.route('/get_th_stat', methods=['GET'])
@cross_origin()
def get_th_stat():
    uri = "https://covid19.th-stat.com/api/open/today"
    try:
        u_response = requests.get(uri)
    except requests.ConnectionError:
        return "Connection Error"
    j_response = u_response.json()
    return j_response


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='3000', debug=True)
