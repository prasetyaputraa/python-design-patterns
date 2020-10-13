import sys
import abc

class AbstractBaseClass(metaclass=abc.ABCMeta):
    def __init__(self):
        print('this abstract class has init method')

    @abc.abstractmethod
    def to_be_overridden(self, new_var):
        self.base_var = new_var

class BaseClass(AbstractBaseClass):
    def __init__(self):
        super().__init__()
        print('a new class')

    def to_be_overridden(self, new_var):
        super().to_be_overridden(20)

        self.new_var = new_var

a = BaseClass()

a.to_be_overridden(10)

print(a.base_var)
print(a.new_var)

