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

    def area(self):
        return self.l * self. b

r = Rectangle(10, 20)

print(r.area())

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

tri = Triangle(10, 1, 2)

print(t)
