class Report:
    def __init__(self,title,content,formatted):
        self.title = title
        self.content = content
        self.formatted = formatted
    def docprint(self):
#        print(f'report - {self.title}, {self.content}')
        self.formatted.format(self)

from abc import ABC, abstractmethod

#Создадим абстрактный класс, который будет служить шаблоном для других классов. Пропишем класс, назвав его Formatted, а указание (ABC) как раз означает, что мы работаем с абстрактными классами,
# то есть мы наследуем класс Formatted от абстракции:
class Formatted(ABC):
# Используем декоратор, с которыми мы уже познакомились ранее.
# Это дополнения к функциям, "обёртки", у которых есть какой-то свой функционал,
# который добавляется в функцию, которую мы прописываем.
# abstractmethod — это декоратор, который прописывается перед той функцией,
# к которой он будет применяться:
    @abstractmethod
# Создадим функцию format и на следующей строке pass, чтобы не выдавалась ошибка:
    def format(self, report): pass

class   TextFormatted:
    def format(self, report):
        print(report.title)
        print(report.content)
class   HtmlFormatted:
    def format(self, report):
        print(f'<h1>{report.title}</h1')
        print(f'<p>{report.content}</p>')

report = Report('title','sdfdfsd lorem ipsum',TextFormatted())
report.docprint()