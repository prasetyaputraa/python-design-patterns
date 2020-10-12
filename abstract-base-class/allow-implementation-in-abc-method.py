import abc
import sys

class Shape(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def implem(self):
        self.a = 'a'
        print('some implementation')

class Rect(Shape):
    def __init__(self):
        pass

    def implem(self):
        super().implem()
        print('additional implementation')

a = Rect()

a.implem()
print(a.a)
