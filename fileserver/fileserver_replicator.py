"""
    * Replicates data to other file servers
    * Contacts the Consul service to determine to who to replicate the data
    * Communicates on a different port compared to the API

    The directory service decides where the data goes
    As a result the replicator will compress the data share a copy to rest of the nodes
    Directory service decides how many files servers

    Might need a stuff like Merkel tree to ensure the consistency of the replica
   

    The fileserver frontend will receive the writes and drop it into the wal 
    logs
"""

import requests
class Replicator():
    def __init__(self, wal, consul_client, app_logger):
       
        # 

        self.wal = wal
        self.consul_client = consul_client
        self.app_logger = app_logger
    def replicate(self):  
        """
            TODO: 
            1. Error handling: what does it do when it cant pass the data to others?
            2. How to handle the consistency i.e. all of them have the right version
                of files ? Merkel trees?
                2.1 do you ignore when majority
        """
        log = self.wal.get()
        if(log) :
           

            for srv in self._get_available_servers():
                r = requests.post(srv, json=log)
              
                self.app_logger.write("Replicated data to {}. Response {}".format(srv,r ))

        else:
            self.app_logger.write("Replicated data to {}. Response {}".format(srv,r ))
    def _get_available_servers(self):
        """
            Returns a list of the addressess of the fileservers
            TODO  return service ports in (addr:port) list pairs 
            
        """

        services = self.consul_client.Consul.Catalog.services()

        return []