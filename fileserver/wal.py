from queue import Queue
class WalEntry():
    def __init__(self, file_id, file_name,
                     created_at, last_modified_at, action):

        self._file_id = file_id
        self._file_name = file_name
        self._created_at = created_at
        self._last_modified_at = last_modified_at
        self._action = action
    @property
    def file_id(self):
        return self._file_id 
    @property
    def file_name(self):
        return self._file_name
    @property
    def created_at(self):
        return self._created_at
    @property
    def last_modified_at(self):
        return self._last_modified_at
    @property
    def action(self):
        return self._action


class WalLogger():
    def __init__(self):
        self.queue = Queue()
    def add_entry(self, wal_entry):
        self.queue.put(wal_entry)
    def get(self):
        """
            Queue throws an exception when there are
            no data, hence the check for size
        """
        if  self.queue.qsize() > 0:
            return self.queue.get()
        else:
            return 0

