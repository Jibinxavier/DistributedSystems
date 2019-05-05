"""
    This module will put together different file server components
    such as
    * API
    * Wal logger
    * Sets up the manager
    2 Consuls :
        * Directory service one - for distributed locking (leader election), storing state
        * FIleserver - Service discovery


    Notes:
        1. Fileserver components will need to connect to different consuls

"""


import consul
import configparser
import wal

def create_consul_client(config='config.ini'):

    config = configparser.ConfigParser()
    config.read('config.ini')

    client = consul.Consul(host=config["FILSERVER_CONSUL"]['HOST'], 
                            port=config["FILSERVER_CONSUL"]['PORT'])
    return client


def build_fileserver():

    consul_client = create_consul_client()
