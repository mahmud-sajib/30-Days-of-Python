## Lesson 15: Class & Object

## Concept: Creating a Class - To define a class, use the class keyword, and define the data points inside.

# Simple class with a property 
class Person:
    name = "John Wick"

## Concept: Creating an Object - o create a new object, simply reference the class you want to build the object out of

# Simple class with a property & an object instance
class Person:
    name = "John Wick"

# creating an object instance
person = Person()

# accessing the class property
print(person.name) #output: John Wick

## Concept: Class Constructor - __init__() method. When we create a class without a constructor, Python automatically creates a default constructor for us that doesn’t do anything. Every class must have a constructor, even if it simply relies on the default constructor

"""
The __init__() function syntax is:

def __init__(self, [arguments])
    1. The 'self' argument refers to the current object. It binds the instance to the init() method. It’s usually named “self” to follow the naming convention.
    2. The init() method [arguments] are optional. We can define a constructor with any number of arguments.
""" 
# Simple class constructor
class Person:
    def __init__(self, person_name):
        self.name = person_name
    
person1 = Person("Johnny Depp")
print(person1.name) # Johnny Depp

person2 = Person("Lora Akintson")
print(person2.name) # Lora Akintson

## Concept: Object Methods

# Simple class with custom method. 'self' is a must use argument in any method inside class.
class Person:
    def __init__(self, person_name, person_job):
        
        self.name = person_name
        self.job = person_job

    def intro(self):
        print(f"{self.name} is a {self.job}")
    
person1 = Person("Johnny Depp", "Actor")
person1.intro() # Johnny Depp is a Actor

person2 = Person("Lora Akintson", "Doctor")
person2.intro() # Lora Akintson is a Doctor



