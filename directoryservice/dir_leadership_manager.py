"""
    This class should run as a separate
    thread. The
    The sole purpose of this class is to manage the leadership behind the scenes.

    * Each server would create a session with consul leader
    * Followed by daemon thread that will keep on polling for leader change
    * Chances of deadlock is reduced by session invalidation on consul which in turn releases lock
    * A leader will periodically renew the session (send-heartbeat)
    * Non-leaders (candidates) will poll the KV on consul


    Notes:
        * Directory service will be the gatekeer of the content on fileservers.It will know where the files are located.
          Hence, it would require it to be relatively more robust
        * Leader election is implemented using Consul
        * Major disadvantage is that this approach uses a lot inherent polling which is not
          scalable 
        
"""
from dir_service_builder import create_consul_client
import consul 
import time
import dateparser
import datetime
import threading 

DEFAULT_PAUSE = 2 # seconds
 
class DirLeadershipManager(threading.Thread):
    def __init__(self, pid, shared_leadership_notifier):
        threading.Thread.__init__(self)
        self.pid = pid
        self.consul_client = create_consul_client()
        self.leadership_acquired = False
        self.shared_leadership_notifier = shared_leadership_notifier # the idea is to point to that object
        # the manager will only write  and the api component will always read this variable to inform itself of change in leadership
        
        self.init_session()
        self.state_transition_controller()
    def init_session(self):
        # Creates a session on consul and throws an exception as its vital to have a session 
        # for leadership in turn consistency 

        self.session_id = self.consul_client.Session.create("Node_"+self.pid, ttl=10)
        if self.session_id  is None:
            raise EnvironmentError("Cannot initate a consul session")

    def run(self):
        # initiates the thread
        self.state_transition_controller()

    def state_transition_controller(self):
        # Works through the state transitions
        while True:
            self.candidate_state()
            self.leader_state()
            time.sleep(DEFAULT_PAUSE + 10)

    
        
    def candidate_state(self ): 
        """
            Candidate state: tries to acquire the lock
        """
        while self.leadership_acquired: 
 
            self.leadership_acquired = self.consul_client.kv.put("dirLeader","Node_"+self.pid, acquire=self.session_id)
            time.sleep(DEFAULT_PAUSE)
        self.shared_leadership_notifier = True

  
        
    def leader_state(self):
        """
            This will update the session so that consul doesn't
            think that this is dead

        """
        pause_time = DEFAULT_PAUSE
        while True:
            resp = self.consul_client.Session.renew(self.session_id)
            # assumed the response is going to be an array
            
            if resp.code != 200:
                print("Failed to renew session")
                # Be good neighbour and release the lock
                self.release_lock()
                break
            expiry = dateparser.parse(resp[0]["TTL"] )
            pause_time = (expiry- datetime.datetime.now()).total_seconds()
            time.sleep(pause_time) # not to flood consul with a lot of polling
    def release_lock(self):
        # here release the lock on the leadership and inform using shared variable 
        # that the leadership has been lost
        self.consul_client.kv.put("dirLeader","Node_"+self.pid, release=self.session_id)
        self.leadership_acquired = False
    def __del__(self):
        self.release_lock()