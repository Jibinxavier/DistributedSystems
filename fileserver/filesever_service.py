
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
        
"""

import json
import threading
import os
import requests as url_request
from flask import Flask, request, jsonify
import consul
import time


import connexion
import datetime
import logging

from connexion import NoContent

mem_storage = {"file1":"heoow"}

def get_files(limit):
    files = mem_storage.keys()[:limit]
    return 


def get_pet(pet_id):
    pet = PETS.get(pet_id)
    return pet or ('Not found', 404)


def put_pet(pet_id, pet):
    exists = pet_id in PETS
    pet['id'] = pet_id
    if exists:
        logging.info('Updating pet %s..', pet_id)
        PETS[pet_id].update(pet)
    else:
        logging.info('Creating pet %s..', pet_id)
        pet['created'] = datetime.datetime.utcnow()
        PETS[pet_id] = pet
    return NoContent, (200 if exists else 201)


def delete_pet(pet_id):
    if pet_id in PETS:
        logging.info('Deleting pet %s..', pet_id)
        del PETS[pet_id]
        return NoContent, 204
    else:
        return NoContent, 404


logging.basicConfig(level=logging.INFO)
app = connexion.App(__name__)
app.add_api('swagger.yaml')
# set the WSGI application callable to allow using uWSGI:
# uwsgi --http :8080 -w app
application = app.app

if __name__ == '__main__':
    # run our standalone gevent server