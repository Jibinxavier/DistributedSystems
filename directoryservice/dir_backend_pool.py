import consul
import configparser
from db_connector.consul_connect import DirServiceBackendConnector
class DirBackendPool():
    """
        Creates a pool of DirServiceBackendConnector objects and manages
        them.

        Parameters:   def   def
            pool_size: Number of objects to be initialised
        
    """
    class __DirBackendPool:
     
        def __init__(self, pool_size=10):
            self.pool_size = int(pool_size)
            
            self.free_objs = []
            self.in_opp_objs = []
            self.__init_pool__()

        def __init_pool__(self):
            """
                Initialise the pool
            """
            for i in range(self.pool_size):
                # build consul client connected to docker 
                obj = create_consul_client()   
                self.free_objs.append(obj)
        def get_obj(self):
            if (len(self.free_objs) > 0):
                obj = self.free_objs.pop()
                self.in_opp_objs.append(obj)
                return obj
            else:
                Exception("Empty object pool")
        def return_obj(self, obj):
            self.free_objs.append(obj)
    
    instance = None
    def __init__(self, pool_size ):
        """
            Will only initialise if not created
        """
        if not DirBackendPool.instance: 
            DirBackendPool.instance = DirBackendPool.__DirBackendPool(pool_size)
         
    def __getattr__(self, name):
        return getattr(self.instance, name)
def create_consul_client(config='config.ini'):

    config = configparser.ConfigParser()
    config.read('config.ini')

    client = consul.Consul(host=config["CONSUL"]['HOST'], 
                            port=config["CONSUL"]['PORT'])
    d = DirServiceBackendConnector(client)
    
    return d