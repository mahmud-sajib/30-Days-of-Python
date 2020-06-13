## Day 22: Python Decorators

## Concept: What is Decorator in Python?

"""
A decorator takes in a function, adds some functionality and returns it.
This is also called metaprogramming because a part of the program tries to modify another part of the program at compile time.
""" 

## Concept: Simple Function Decorator

# A Simple Decorator
def weatherCondition(func):
    def status():
        print("Hey, It's raining!")
        func()
    return status

def statOne():
    print("I am not going outside.")

statOne = weatherCondition(statOne)
statOne() # output: Hey, It's raining! I am not going outside.

def statTwo():
    print("I would love to walk in the rain.")

statTwo = weatherCondition(statTwo)
statTwo() # output: Hey, It's raining! I would love to walk in the rain.

"""
In the above examples 'weatherCondition()' is a decorator function that adds some new functionality to the original functions 'statOne()' & 'statTwo()'.
"""

"""
We can use the @ symbol along with the name of the decorator function and place it above the definition of the function to be decorated
"""

@weatherCondition
def statThree():
    print("I need an umbrella to go outside!")

statThree() # output: Hey, It's raining! I need an umbrella to go outside!

## Concept: Decorating Functions with Parameters

# A Simple Decorator with Parameterized Functions
def numDivider(func):
    def inner(a,b):
        print("I am going to divide", a, "by", b)
        if b == 0:
            print("Whoops! cannot divide")
            return
        return func(a,b)
    return inner

@numDivider
def divideOne(a,b):
    print(a/b)

divideOne(100,5) # output: I am going to divide 10 by 5. 2.0

@numDivider
def divideTwo(a,b):
    print(a/b)

divideTwo(10,0) # output: I am going to divide 10 by 0. Whoops! cannot divide

"""
Explaination: First we call the 'numDivider()' function and pass 'divideOne' as a parameter so it looks like 'numDivider(divideOne)'. Now, this returns the 'inner()' function which has not been executed [since inner() was not called].

Next we call 'divideOne(param1, param2)' & that moment the 'inner()' function is called and returns the output of 'divideOne(param1, param2)' function.
"""

## Concept: Chaining Decorators in Python

"""
Multiple decorators can be chained in Python.
This is to say, a function can be decorated multiple times with different (or same) decorators. 
We simply place the decorators above the desired function.
"""

def star(func):
    def wrapper(*args, **kwargs):
        print("*" * 10)
        func(*args, **kwargs)
        print("*" * 10)
    return wrapper

def wave(func):
    def wrapper(*args, **kwargs):
        print("~" * 30)
        func(*args, **kwargs)
        print("~" * 30)
    return wrapper


@star
@wave
def greet(msg, name):
    print(f"{msg} {name}")

greet("Hello", "John")

"""
The above syntax of:

@star
@wave
def greet(msg, name):
    print(f"{msg} {name}")

is equivalent to:

def greet(msg, name):
    print(f"{msg} {name}")
printer = star(wave(printer))

Here, first the 'wave()' decorator will enclose & decorate the 'greet()' function output with '~' sign. 
Then the resultant output will be entirely enclosed & decorated by 'star()' decorator with '*' sign.
"""


