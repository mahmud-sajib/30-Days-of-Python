## Day 20: Python Generators

## What are generators in Python?

"""
Python generators are a simple way of creating iterators.
A generator is a function that returns an object (iterator) which we can iterate over (one value at a time).
"""
## How to create a generator in Python?

"""
It is the same as defining a normal function, but with a 'yield' statement instead of a 'return' statement.
The difference is that while a return statement terminates a function entirely, 
yield statement pauses the function saving all its states and later continues from there on successive calls.
"""

# Example of a generator
def my_iterable():
    i = 5
    while i > 0:
        yield i
        i -= 1

num = my_iterable()

# we can use next() to access values from generators
print(next(num)) # 5
print(next(num)) # 4

# alternatively we can use loop to access all the values at a time.
for i in my_iterable():
    print(i)

# output: 5 4 3 2 1