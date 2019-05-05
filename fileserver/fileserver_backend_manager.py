"""
    This class manages connectivity to consul registers with 


    Responsible for:
        * Registering with consul service discovery
        * Sending health chekcs 

 
    Setup with a tcp listner for health checks
"""
import threading 
import consul
import socket
import sys

class FileserverBackendManager(threading.Thread):
    def __init__(self, consul_client, ip, api_port ):
        threading.Thread.__init__(self)
        self.consul_client = consul_client # pass in the correct config 
        self.ip = ip
        self.api_port = api_port

        num_fileservers = 0
        
        consul_check_def = consul.Check.tcp( self.ip,self.api_port, 10, timeout=12, deregister=15)
        num_fileservers = self.consul_client.Catalog.services()
        self.consul_client.Service.register( "Fileserver_{}".format(num_fileservers), 
            address=self.ip,
            port=self.api_port,
            check= consul_check_def, 
            meta="fileserver")

    def run(self):
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_address = ('localhost', 8080)
	print( 'Listener starting up on {} port: '.format(server_address), file=sys.stderr)
	sock.bind(server_address)
	sock.listen(1)
	while True:
	    # Wait for a connection
			
	    print( 'waiting for a connection', file=sys.stderr)
            connection, client_address = sock.accept()
	    try:
		print( 'connection',client_address, file=sys.stderr)
		

		# Receive the data in small chunks and retransmit it
		while True:
		    data = connection.recv(16)
		    print(data)
		    if data:
					
			connection.sendall(b"ok")
		    else:
			print('no more data from',client_address, file=sys.stderr)
						
		        break
					
	    finally:
		# Clean up the connection
		connection.close()
