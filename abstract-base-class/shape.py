import sys
import abc

class Shape(metaclass=abc.ABCMeta):
    """
    [] An abstract class is a class that contains abstract methods.
        [] An abstract method is a method which is declared,
            but contain no implementations
        [] A subclass of Abstract Classes must implement
            the abstract method
    """
    @abc.abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, x, y):
        self.l = x
        self.b = y

        print(x)

    def area(self):
        return self.l * self. b

class Triangle(Shape):
    """
    [] This will result a TypeError,
        because this class doesn't implement area abstract method
        from the superclass
    """
    def __init__(self, hypothenus, opposite, adjacent):
        self.h = hypothenus
        self.o = opposite
        self.a = adjacent

try:
    r = Rectangle(10, 20)

    print(r)
    
    print(r.area())
except:
    print(sys.exc_info()[0])

try:
    tri = Triangle(10, 1, 2)

    """
    The class won't even instantiate
    because it was missing the implemnetation
    of one or more abstract methods
    of its superclass
    """
    print(tri)
except:
    print(sys.exc_info()[0])
