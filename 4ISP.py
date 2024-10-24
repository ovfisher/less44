# Принцип разделения интерфейсов (ISP, Interface Segregation Principle)
#
# не должно быть зависимостей от интерфейсов, которые они не используют.
# Суть в создании специализированных интерфейсов вместо одного, делающего всё подряд.
# Это упрощает внедрение зависимостей и повышает гибкость системы. Объекты в программе
# должны быть заменяемыми на экземпляры подтипов без влияния на правильность программы.
# Это значит, что объекты производного класса должны иметь возможность заменить объекты
# базового класса без изменения работы программы.
class SmartHouse():
    def turn_on_light(self): pass
    def heat_food(self): pass
    def turn_on_music(self): pass
# Согласно принципу разделения интерфейсов нам нужно прописать все эти функции по отдельности,
# как бы сделав для каждого устройства отдельный пульт. Для этого нужно создать каждой функции
# отдельный класс.
#
# class Light():
# def turn_on_light(self):
# print("Свет включен")
#
# class Food():
# def heat_food(self):
# print("Еда начала разогреваться")

# class Music():
# def turn_on_music(self):
# print("Включаю подборку ваших любимых песен")