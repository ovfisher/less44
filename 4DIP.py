# Принцип инверсии зависимости (DIP, Dependency Inversion Principle)
#
# Модули высокого уровня не должны зависеть от модулей низкого уровня.
# Оба типа модулей должны зависеть от абстракций.
# Абстракции не должны зависеть от деталей; детали должны зависеть от абстракций.
# Это позволяет разрабатывать систему более гибкой и способствует её лёгкому тестированию.
# Создадим базовый класс Book:
# пример, в котором не используется данный принцип
class Book_:
    def read(self): print("Чтение интересной истории")

class StoryReader_:
    def init(self): self.book = Book_()

# Обычно две части не должны связываться между собой.  .... так делать не надо.

from abc import ABC, abstractmethod
class StorySource(ABC):
    @abstractmethod
    def get_story(self): pass

class Book(StorySource):
    def get_story(self): print("Чтение интересной истории")

class StoryReader :
    def __init__(self, story_source: StorySource):
        self.story_source = story_source

    def get_story(self):
        print("Чтение интересной истории")

    def tell_story(self):
        self.story_source.get_story()

class AudioBook(StorySource):
     def get_story(self):
        print("Чтение интересной истории вслух")

book = Book()
audioBook = AudioBook()
readerBook = StoryReader(book)
readerAudioBook = StoryReader(audioBook)
readerBook.tell_story()

readerAudioBook.tell_story()