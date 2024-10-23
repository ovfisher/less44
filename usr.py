#class UM:
#    def __init__(self,user):
#        self.user = user
#    def change_user_name(self, uname):
#        self.name = uname
#    def save_user(self):
#        file = open('users.txt', 'a')
#        file.write(self.user)
#        file.close()

class Usr:
    def __init__(self,user):
        self.user = user
class Usrnamechanger:
    def __init__(self,user):
        self.user = user
    def change_name(self, name):
        self.name = name
class Saveuser:
    def __init__(self,user):
        self.user = user
    def save(self):
        file = open('users.txt', 'a')
        file.write(self.user)
        file.close()