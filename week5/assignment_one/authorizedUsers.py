import users
class AuthorizedUsers(users.User):
    
    def __init__(self):
        self.authorized_users = []
    
    def addUser(self, user):
        self.authorized_users.append(user)

    @staticmethod
    def print_authorized_users(self):
        for user in self.authorized_users:
            print(user)
    
    
    
