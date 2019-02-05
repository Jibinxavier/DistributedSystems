from pymongo import MongoClient 
"""
1: successful signup
2: User already exists
3: True/False authenticated
4: User does not exists
"""


class UserDb:
    def __init__(self,host="localhost",port=27017, collection):
        self.client = MongoClient(host,port)
        self.db = self.client['user-db']
        self.collection = self.db['user_collection']
    def insert(self, doc):
        self.collection.insert_one(doc)
        return  {"message":"Signup successful", "code": 1}
    def signup(self, username, password):
        doc  = { 'username': username, 'password': password }
        user = self.collection.find_one({ 'username': username } )
        if user:  
            return  {"message":"User already exists", "code": 2}
        else:
            return self.insert(doc)
        
    def is_authorised(self, username, password): 
        user = self.collection.find_one({ 'username': username } )
        if user:  
            print(user)
            return {"message":str( user['password']==password), "code": 3}
        else:
            return  {"message":"User doesn't exist", "code": 4} 
    def _clear_collection(self, collection):
        self.db[collection].drop()