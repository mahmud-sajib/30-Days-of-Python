## Day 26: Polymorphism

# Class Polymorphism in Python

class Beatles:
    def __init__(self, genre, origin):
        self.genre = genre
        self.origin = origin

    def info(self):
        print(f"Beatles is a {self.genre} band based in {self.origin}")
    

class Lalon:
    def __init__(self, genre, origin):
        self.genre = genre
        self.origin = origin

    def info(self):
        print(f"Lalon is a {self.genre} band based in {self.origin}")

beatles = Beatles("Rock", "USA")
lalon = Lalon("Folk", "Bangladesh")


for band in (beatles, lalon):
    band.info()

# Beatles is a Rock band based in USA
# Lalon is a Folk band based in Bangladesh

"""
Here, we have created two classes Beatles & Lalon. They share a similar structure and have the same method names info().
However, notice that we have not created a common superclass or linked the classes together in any way. Even then, we can pack these two different objects into a tuple and iterate through it using a common 'band' variable. It is possible due to polymorphism.
"""

# Polymorphism and Inheritance (Method Overriding)

class Shape:
    def __init__(self, name):
        self.name = name


class Square(Shape):
    def __init__(self, name, length):
        super().__init__(name)
        self.length = length

    def area(self):
        print(f"Area of {self.name} is {self.length**2}") 


class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        print(f"Area of {self.name} is {3.1416*self.radius**2}")

obj1 = Square('Square', 10)
obj1.area()

obj2 = Circle('Circle', 5)
obj2.area()

# Area of Square is 100
# Area of Circle is 78.53

"""
Due to polymorphism, the Python interpreter automatically recognizes that which area() method is associated with Square/Circle class and override them accordingly.
"""
