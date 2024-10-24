# 1 Принцип единственной ответственности (SRP, Single Responsibility Principle)
# каждый класс должен иметь только одну причину для изменения.
# => класс должен выполнять только одну задачу или иметь только одну
# область ответственности. Это упрощает тестирование и поддержку кода.

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