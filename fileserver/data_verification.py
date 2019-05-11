"""
    This file will have the merkle tree implementation
    and API to verify the local data


"""
import datetime
from collections import namedtuple
Hash = namedtuple('Hash', 'hash time_stmp')
class Validator():
    def __init__(self, fileserver):
        """
            Intiate the data structure
        """
        self.merkletree = MerkleTree()
        pass
    def validate(self, root):
            
        return self.merkletree.root_hash == root_hash


class MerkleTree():
    
    def __init__(self, root_hash,)
        self._root_hash = root_hash
        self._prev_hashes = []
    @property
    def root_hash(self):
        return self._root_hash
    def __re_cal_rhash(self):
        """ 
            Update to the tree would require 
            recalculation of the datastructure
            TODO
        """
        time_stp = datetime.datetime.now()
        self._prev_hashes.append(Hash(self.root_hash, time_stmp))
        
    def insert(self, node):
        """
            Implementation  TODO
        """
        self.__re_cal_rhash()

    def delete(self, hash):
        """
            Implementation  TODO
        """
        self.__re_cal_rhash()
    def display_existing_tree()
class Node():
    """
        l_node = left node
        r_node = right node
        hash_v = hashed value
        level = is its position in the tree structure, e.g root being 0, left and right nodes will be both 1
        metadata = additional metadata structure, could be used to store for example file name
            - merkle tree will be used to check the integrity of the replicas
            - by doing this it will be easy to identify
        s 
    """
    def __init__(self, l_node, r_node, hash_v, level,metadata, num_child=0):
        self.l_node = l_node
        self.r_node = r_node
        self.hash_v = hash_v
        self.level = level
        self.metadata = metadata
        self.num_child = num_child
    

