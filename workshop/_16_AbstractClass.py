# we can use from abc import * asterisk for all import

from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod  # Decorator or annotation
    def area(self):  # Empty function which has pass
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side*self.__side

    def perimeter(self):
        return self.__side*4

# shape_obj = Shape() # error here


square_obj = Square(10)
print(square_obj.area())
print(square_obj.perimeter())