from common.utils import UserDb


class TestUserDb(UserDb):
    def __init__(self,host="localhost",port=27017):
        super().__init__(host,port, "test-collection")
    def find_user(self, username):
        user = self.collection.find_one({ 'username': username } )
        return user

    

