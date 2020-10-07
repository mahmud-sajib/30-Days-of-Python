## Day 26: Abstract Class

"""
In Python to use Abstract classe we have to import 'ABC' module.
To make a Class Abstract We inherit from 'ABC' class. We can't instantiate object from Abstract Class. 
Abstract methods have no body. We define Abstract methods with @abstractmethod decorator.
"""

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        print(f"Area of Square is {self.length**2}") 


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(f"Area of Circle is {3.1416*self.radius**2}")

obj1 = Square(10)
obj1.area()

obj2 = Circle(5)
obj2.area()

# Area of Square is 100
# Area of Circle is 78.53

