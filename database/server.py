"""
    login with oauth example Google
    
"""


import base64
import hashlib
import json
import random

import time
import os
import sys
import queue 
from subprocess import call,check_output
from flask import Flask,jsonify,request
from common.utils import UserDb

 

app = Flask(__name__) 




db =  UserDb()
@app.route('/user/signup', methods=['POST'])
def signup_user():
 
    data = request.get_json() 
    if len(data) >0 :
        print(db.signup( data["username"],data["password"]))
        return jsonify({"message":"ok", "code": 5}) 
    else:
        return jsonify({"message":"failed", "code": 0})
    

@app.route('/user/login', methods=['POST'])
def login_user():
     
    data = request.get_json() 
    if len(data) >0 :
        
        return jsonify(db.is_authorised( data["username"],data["password"]))
    else:
        return jsonify({"message":"failed", "code": 0})
def standup_db():
    cmd_out = str(check_output(["docker", "ps"]))

    if "mongo" not in cmd_out:
        print("Standing up mongodb database")
        call(["docker", "run","--name", "mongodb", "-d", "--network","host", "mongo", ])
        #call(["docker", "run", "--rm", "-d", "--network","host", "mongo", "--name", "mongodb"])
    print("Database already setup")

if __name__ == "__main__": 
    #docker run --rm -d --network host 
    standup_db()
    app.run(host='0.0.0.0', port=8080, debug=True)