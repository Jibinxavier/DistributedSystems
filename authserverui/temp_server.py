"""
    THis would act the way how the file server API
    would respond
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
 

 

app = Flask(__name__) 
 



@app.route('/files', methods=['get'])
def get_files():
    temp_data = { "file1": "file1/path",  "file2": "file2/path" ,  "file3": "file3/path"}
    return 
    
 
if __name__ == "__main__": 
    #docker run --rm -d --network host 
 
    app.run(host='0.0.0.0', port=9001, debug=True)