

import abc
from abc import ABC, abstractmethod

 
class ConsulInterface():
    
    @abstractmethod
    def read_key():
        pass
    @abstractmethod
    def insert_key():
        pass