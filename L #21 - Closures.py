## Day 21: Python Closures

## Concept: Understanding Nested Function

"""
Before getting into what a closure is, we have to first understand what a nested function and nonlocal variable is.
A function defined inside another function is called a nested function. Nested functions can access variables of the enclosing scope.
"""

# Following is an example of a nested function accessing a non-local variable.
# This is the outer enclosing function
def print_msg(msg):
    
    # This is the nested function
    def my_print():
        print(msg)
    
    my_print()

print_msg("Hi") # output: Hi
print_msg("Bye") # output: Bye

"""
We can see that the nested printer() function was able to access the non-local msg variable of the outer enclosing function.
"""

## Concept: Defining a Closure Function

"""
In the example above, what would happen if the last line of the function print_msg() returned the my_print() function instead of calling it? This means the function was defined as follows.
"""

def print_msg(msg):
    
    # This is the nested function
    def my_print():
        print(msg)
    
    return my_print

hi = print_msg("Hi") 
hi() # output: Hi

bye = print_msg("Bye") 
bye() # output: Bye

"""
That's unusual.

The print_msg() function was called with the string 'Hi' and the returned function was bound to the name 'hi'. On calling hi(), the 'msg' variable was still remembered although we had already finished executing the print_msg() function.

This technique by which some data ('Hi' in this case) gets attached to the code is called 'Closure' in Python.
"""

## Concept: When to use closures?

# A simple example where a closure might be more preferable than defining a class and making objects.

def make_sqaure(n):
    def square():
        print(n**2)
    
    return square

square_of_5 = make_sqaure(5)
square_of_5() # output: 25

square_of_10 = make_sqaure(10)
square_of_10() # output: 100

"""
Here, first we call the 'make_sqaure()' function & pass the value(e.g. 5) it just returns the 'square' function that was waiting to be executed. We assign 'make_sqaure()' to a variable 'square_of_5' then we turn it to a function & call that function. At that moment our awaiting 'square()' function is executed and print the expected result.
"""


