## Day 19: Python Iterators

## Concept: What are iterators in Python?

"""
Iterator in Python is simply an object that can be iterated upon. 
An object which will return data, one element at a time.
Technically speaking, Python iterator object must implement two special methods, __iter__() and __next__(), collectively called the iterator protocol.
An object is called iterable if we can get an iterator from it. 
Most of built-in containers in Python like: list, tuple, string etc. are iterables.
"""

## Concept: Iterating Through an Iterator in Python

"""
We use the next() function to manually iterate through all the items of an iterator. 
When we reach the end and there is no more data to be returned, it will raise 'StopIteration'
"""

# define a list
nums = [4, 7, 0, 3]

# get an iterator using iter()
nums_iterator = iter(nums)

# iterate through the iterator using next()
print(next(nums_iterator)) # output: 4

# iterate through the iterator using next()
print(next(nums_iterator)) # output: 7

# iterate through the iterator using __next__() [ which is similar to next() ]
print(nums_iterator.__next__()) # output: 0

# iterate through the iterator using __next__() [ which is similar to next() ]
print(nums_iterator.__next__()) # output: 3

# attempting to iterate when the iterator already reached to it's end
print(nums_iterator.__next__()) # raised StopIteration exception

""" for loop is a more elegant way of automatically iterating through any iterator"""

## Concept: Building Your Own Iterator in Python

"""
Building an iterator from scratch is easy in Python. We just have to implement the methods __iter__() and __next__().
The __iter__() method returns the iterator object itself.
The __next__() method keeps the state of current item internally & return the next item. At the end, and in subsequent calls, it must raise StopIteration.
"""

class PowNum:
    """Class to implement an iterator to output power of numbers"""

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self): 
        # iteration starts from 1 & runs upto 5
        if self.num <= 5:
            # get the value 
            result = self.num ** 2
            # go to the next value
            self.num += 1
            # return the result
            return result
        else:
            raise StopIteration

obj = PowNum()
i = iter(obj)
print(next(i)) # 1
print(next(i)) # 4
print(next(i)) # 9
print(next(i)) # 16
print(next(i)) # 25
print(next(i)) # raise StopIteration

        

