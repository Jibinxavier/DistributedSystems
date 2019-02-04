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
 
from pymongo import MongoClient 
 

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
        self.db = self.client['user-db']
        self.user_collection = self.db['user_collection']
    def insert(self, doc):
        self.user_collection.insert_one(doc)
        return  {"message":"Signup successful", "code": 1}
    def signup(self, username, password):
        doc  = { 'username': username, 'password': password }
        user = self.user_collection.find_one({ 'username': username } )
        if user:  
            return  {"message":"User already exists", "code": 2}
        else:
            return self.insert(doc)
        
    def is_authorised(self, username, password): 
        user = self.user_collection.find_one({ 'username': username } )
        if user:  
            print(user)
            return {"message":str( user['password']==password), "code": 3}
        else:
            return  {"message":"User doesn't exist", "code": 4} 

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