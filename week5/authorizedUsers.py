import users
class AuthorizedUsers(users.User):
    LIST_OF_AUTHORIZED_USERS = []
    def __init__(self, firstName, lastName, email ):
        users.User.__init__(self, firstName= firstName, lastName=lastName, email=email,)
        authorized_user = {"fName": f"{self.firstName}", "lName": f"{self.lastName}", "email": f"{self.email}"}
        self.LIST_OF_AUTHORIZED_USERS.append(authorized_user)
    
    @staticmethod
    def print_authorized_users():
        return AuthorizedUsers.LIST_OF_AUTHORIZED_USERS


