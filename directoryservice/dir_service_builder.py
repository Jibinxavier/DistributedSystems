"""
    This class will put together the following components 
    for the directory service.

    The major components 
     
"""
import configparser
import consul

from dir_backend_pool import DirBackendPool
def create_consul_client(config='config.ini'):

    config = configparser.ConfigParser()
    config.read('config.ini')

    client = consul.Consul(host=config["CONSUL"]['HOST'], 
                            port=config["CONSUL"]['PORT'])
    return client
def get_backend_pool(config='config.ini'):
    """
        TODO: Double check if its returning the same object
    """
    config = configparser.ConfigParser()
    config.read('config.ini')
  
    return  DirBackendPool(config["CONSUL"]["POOL_SIZE"])

 