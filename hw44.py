class Fighter:
    def __init__(self,name,weapon):
        self.name = name
        self.weapon = weapon
        print('init')
    def change_weapon(self, weapon):
        self.weapon = weapon
        print(f'arms with {weapon.name}')
        self.weapon.attack(self)

from abc import ABC, abstractmethod
class Weapon(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def attack(self, Fighter): pass

class Sword(Weapon):
    def attack(self, Fighter):
        print('hit by sword,Victory!')
class Bow(Weapon):
    def attack(self, Fighter):
        print('bow shooting,Victory!')
class Lance(Weapon):
    def attack(self, Fighter):
        print('hit by lance,Victory!')

class Monster:
    def __init__(self, name):
        self.name = name

f1 = Fighter('Hercules',Sword('sword'))
f1.change_weapon(Bow('bow'))
f1.change_weapon(Lance('lance'))
