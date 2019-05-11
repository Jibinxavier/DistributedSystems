
#!/usr/bin/env python3
"""
    Responsible for:
        * Serving API and responding to client requests 
        * Writes have to written and replicated into WAL log
        * Maintaining merkele tree for replica consistency
    
    TODO:

    * Need a mechanism to store the metadata of the files in 
    memory so that its faster retrieve and merkele tree stuff
    * Need state diagram stuff that will initialise when a server
    starts up
        * Need to integrate the failure recovery stuff 
    
    * Need to test how different file types will work e.g jpg
    Fileserver workflow
        * Each file will be stored under fileserver
        * THe directory server will have all
"""

import json
import threading
import os
import requests as url_request
from flask import Flask, request, jsonify, send_from_directory
import consul
import time


import connexion
import datetime
import logging

from connexion import NoContent

mem_storage = {"file1":"heoow"}

FILES_DIR = "./fileserver"
def setup_file_dirs():
    """
        Setup file directory components such as:
         * storage directory
        
    """
    file_dir = "./fileserver"
    if os.path.isdir(file_dir):

        os.mkdir(file_dir)

 



def get_file(file_id):
    """
        TODO: authorisation
    """

    file = FILES_DIR+file_id
    if os.path.isfile(file):
        return send_from_directory(FILES_DIR, file_id, as_attachment=True )
    else:
        return ('Not found', 404)


def put_file(file_id, content):
    file = FILES_DIR+file_id
    if os.path.isfile(file): 
        logging.info('Updating file %s..', file_id)
        
    else:
       logging.info('Creating file  %s..', file_id)
    with open(file, "w+")as f:
        f.write(content)
    return NoContent, (200 )


def delete_file(file_id):
    file = FILES_DIR+file_id
    if os.path.isfile(file):
        logging.info('Deleting file %s..', file_id)
        os.remove(file)
        return NoContent, 204
    else:
        return NoContent, 404


def put_rep_file(file_id, directory, content):
    """
        TODO: authorisation -making sure there is some endpoint protection
         are sure you are talking to the right server
         mutual tls?
         2. Consistency- merkele tree and stuff like that 
    """
    file =  directory+file_id
    logging.info('Deleting file %s..', file_id)
    with open(file) as f:
        f.write(content)
    return NoContent, 204
if __name__ == '__main__':
    # run our standalone gevent server
    logging.basicConfig(level=logging.INFO)
    app = connexion.App(__name__)
    app.add_api('swagger.yaml')
    # set the WSGI application callable to allow using uWSGI:
    # uwsgi --http :8080 -w app
    application = app.app
