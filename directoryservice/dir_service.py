
import json
import threading
import os
import requests as url_request
from flask import Flask, request, jsonify
from dir_service_builder import get_backend_pool
import consul 
import time
"""


How the directory service deals with File servers?


 * Directory servers have a list of directories where clients can store
 * They could be namd (f1, id=1), (f2, id=2) and (f3, id=3)
 * And use consistent hashing (why? I don't yet)
    * This would make the file server more transparent 
    * Variants of consistent hashing could be implemented including storing the data close to the client, thus reducing latency


 * failure recovery: Part of the data will be replicated to other servers


"""


app = Flask(__name__)
@app.route('/v1/dirs', methods=['GET'])
def list_dirs():
    db_conn = get_backend_pool().get_obj()
     
 
    return jsonify({})
     
@app.route('/v1/files/', methods=['GET'])
def list_fs_contents():
    obj = get_backend_pool()
    print(obj )
    
    return jsonify({})
@app.route('/v1/cluster/join', methods=['post'])
def cluster_join(self)):
    """
        Metadata should include :
         *ip
         *
    """
    obj = get_backend_pool()
    print(obj )
    
    return jsonify({})
 
     
 
if __name__=="__main__":
     
    app.run(host='0.0.0.0', debug=True)

