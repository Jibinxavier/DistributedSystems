
import json
import threading
import os
import requests as url_request
from flask import Flask, request, jsonify
import consul
import time
"""

    
*
"""



import connexion

app = connexion.App(__name__, specification_dir='swagger/')
app.add_api('fileserver_api.yaml')
app.run(port=8080)