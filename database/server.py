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
from flask import Flask
from flask import jsonify
from flask import request
from pymongo import MongoClient 
from flask import Flask 


app = Flask(__name__) 


"""
1: successful signup
2: User already exists
3: True/False authenticated
4: User does not exists
"""

class UserDb:
    def __init__(self,host="localhost",port=27017):
        self.client = MongoClient(host,port)
        self.db = self.client['user']
    def insert(self, doc):
        self.db.insert_one(doc)
        return (1, "Signup successful ")
    def signup(self, userid, passw):
        doc  = { 'userid': userid, 'passw': passw }
        user = self.db.find_one({ 'userid': userid } )
        if user:  
            return (2, "User already exists")
        else:
            return self.insert(doc)
        
    def is_authorised(self, userid, passw): 
        user = self.db.find_one({ 'userid': userid } )
        if user: 
            return (3, user[passw]==passw)
        else:
            return (4, "User doesn't exist")


db =  UserDb()
@app.route('/user/signup', methods=['POST'])
def signup_user():
    data = request.get_json(force=True)
    print(db.signup( data["userid"],data["passw"]))
    return 'ok'
    

@app.route('/user/login', methods=['POST'])
def login_user():
    data = request.get_json(force=True)
    print(db.is_authorised( data["userid"],data["passw"]))
    return db.is_authorised( data["userid"],data["passw"])
def standup_db():
    cmd_out = str(check_output(["docker", "ps"]))

    if "mongo" not in cmd_out:
        print("Standing up mongodb database")
        call(["docker", "run", "--rm", "-d", "--network","host", "mongo", "--name", "mongodb"])
    print("Database already setup")

if __name__ == "__main__": 
    #docker run --rm -d --network host 
    standup_db()
    app.run(host='0.0.0.0', port=8080)