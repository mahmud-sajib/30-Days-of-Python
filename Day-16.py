## Day 16: First Class Functions and Lambda Expressions

## Concept: What are first class functions?
""" In Python, functions are first class object (first class citizen too!). Programming language theorists defined some criteria for first class object of a programming language. A “first class object” is a program entity which can be :
    1. created at run time
    2. can be assigned to a variable
    3. can be passed as function argument
    4. can be returned from a function
"""


## Concept: Function Creation in run time

# runtime function calling (recursively)
def print_inversely(n):
    print(n, end=" ")
    if n > 0:
        print_inversely(n - 1)

print_inversely(10) 
# output: 10 9 8 7 6 5 4 3 2 1 0

"""
Here, we have a recursive function named print_inversely which will print n down to 0. 
Number of calls of print_inversely function depends on value of n. 
Depending on value of n it calls itself. 
Before running the program it cannot decide about its behavior, number of calls etc. 
At the run time it calls itself recursively depending on the value of n. 
In other word, “here we are creating and calling the function at run time.
"""

# In Python, functions are object too. Here 'print_inversely' function is an instance of function class
def print_inversely(n):
    print(n, end=" ")
    if n > 0:
        print_inversely(n - 1)

print(type(print_inversely)) 
# output: <class 'function'>

## Concept: Assigning function to a variable

def print_inversely(n):
    print(n, end=", ")
    if n > 0:
        print_inversely(n - 1)

# assigning to a variable
our_first_class_function = print_inversely

# call function through variable
our_first_class_function(15) 
# output: call function through variable

## Concept: Passing functions as argument

def print_inversely(n):
    print(n, end=" ")
    if n > 0:
        print_inversely(n - 1)


def print_inversely_by_user_input(func): 
    n = int(input("\n Please input a number to start: "))
    # call the print_inversely' function
    func(n)

# takes 'print_inversely' function as an argument
print_inversely_by_user_input(print_inversely)

"""
Here 'print_inversely_by_user_input' function takes 'print_inversely' function as argument. 
the new print_inversely_by_user_input' function takes an integer user input and call the print_inversely' function.
"""

## Concept: Returning function from function

def ever_or_odd(n):
    def even():
        print(f"{n} is even")
    
    def odd():
        print(f"{n} is odd")

    if n % 2 == 0:
        return even()
    else:
        return odd()

n = int(input("Write a integer to check: "))
ever_or_odd(n)

""" 
ever_or_odd function returns a function depending of value of n. 
If we pass an even number to n, then it will return reference of even() function otherwise it will return reference of odd() function. 
Hence, a function is returning another function!
"""


    








