"""
 * Directory service
 * 
"""
from .consul_interface import  ConsulInterface
 
class DirServiceBackendConnector(ConsulInterface):
    """
        This handles the connection between the consuls 
        backend storage
    """
    def __init__(self, client):
        """
        """
        self.consul_client = client
        
    def read_file(self, key):
        
        """
            TODO: Need to check what sort of content is returned back,
            how does it handle the errors, and exception handling 
            try catch and finally. Lastly the logging aspect of things


            @key: path to the value
            returns: contents on that path 
        
        """
        index = None
        index, data = self.consul_client.kv.get(key , index=index)

        return data['Value']
    def write_file(self, key, value):
        """
            TODO: Error handling as above
            @key: path to the value
            @value: content to be stored
            returns: Success or failure
        """
        self.consul_client.kv.put(key, value)

   