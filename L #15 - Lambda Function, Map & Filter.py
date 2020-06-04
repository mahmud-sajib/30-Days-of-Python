## Day 15: Lambda Function, Map & Filter

## Concept: What are lambda functions in Python?
"""
In Python, an anonymous function is a function that is defined without a name.
While normal functions are defined using the def keyword in Python, anonymous functions are defined using the lambda keyword.
Hence, anonymous functions are also called lambda functions.
"""

# Simple Lambda Function to print square of a number. This function has no name. It returns a function object which is assigned to the identifier square.
square = lambda x: x**2
print(square(5)) # output: 25

# The above Lambda Function is nearly the same as:
def square(x):
    return x**2
square(5)

## Concept: Use of Lambda Function in python
"""
In Python, we generally use use lambda functions as an argument to a higher-order function (a function that takes in other functions as arguments). 
Lambda functions are used along with built-in functions like filter(), map() etc.
"""

# Example use with filter()
"""
The filter() function takes in a 'function' and a 'list' as arguments.
filter() takes all elements in the list and returns a new list is which contains elements for which the function evaluates to 'True'.
"""
# use of filter() to filter out only even numbers from a list.
my_list = [1, 2, 3, 4, 5]
new_list = list(filter(lambda n: (n % 2 == 0), my_list))
print(new_list)
# output: [2, 4] (returns only '2' & '4' since they are the only even numbers in the list)

# use of map() to filter out which numbers can be squared. 
my_list = [1, 2, 3, 4, 5]
new_list = list(map(lambda n: n**2 , my_list))
print(new_list)
# output: [1, 4, 9, 16, 25] (returns all the elements since each of them can be squared.)

# Example use with map()
"""
The map() function takes in a 'function' and a 'list' as arguments.
map() takes all elements in the list and allows us to apply the function to them & returns a new list.
"""

# use of map() to check even numbers
my_list = [1, 2, 3, 4, 5]
new_list = list(map(lambda n: (n % 2 == 0), my_list))
print(new_list)
# output: [False, True, False, True, False] (returns 'Truth' value since with the function call each element evaluates to either 'true' or 'false')

# use of map() to suare all the items in a list 
my_list = [1, 2, 3, 4, 5]
new_list = list(map(lambda n: n**2 , my_list))
print(new_list)
# output: [1, 4, 9, 16, 25] (returns the squared value of each element)