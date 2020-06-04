## Day 16: Flexible Functions with *args & **kwargs

## Concept: What is *args and **kwargs ?

"""*args and **kwargs allow us to pass multiple arguments or keyword arguments to a function."""

## Concept: Using **args in Function Definition

"""Consider the following example. This is a simple function that takes two arguments and returns their sum. This function works fine, but it’s limited to only two arguments."""
def sum_of_num(a, b):
    return a + b

"""
What if we need to sum a varying number of arguments, where the specific number of arguments passed is only determined at runtime? 
This is where *args can be really useful, because it allows us to pass a varying number of positional arguments.
"""

"""Consider the following example. We’re passing three different positional arguments. sum() takes all the parameters that are provided in the input and packs them all into a single iterable object named 'args'."""
def sum_of_num(*args):
    result = 0
    for n in args:
        result += n
    print(result)

sum_of_num(1,2,3) # output: 6

"""
'args' is just a name. We can choose any name that we prefer. All that matters here is that you use the unpacking operator (*).
Note that the iterable object we’ll get using the unpacking operator * is 'not a list' but 'a tuple'.
"""

## Concept: Using **kwargs in Function Definition

""" **kwargs works just like *args, but instead of accepting positional arguments it accepts keyword (or named) arguments."""

"""Take the following example, concatenate() will iterate through the Python kwargs dictionary and concatenate all the values it finds."""
def concatenate(**kwargs):
    print(type(kwargs))
    result = ""
    for kwarg in kwargs.values():
        result = result + kwarg
    print(result)

concatenate(a="SpaceX ", b="& ", c="NASA ", d="launched ", e="rocket.")

"""
'kwargs' is just a name. We can choose any name that we prefer. All that matters here is that you use the unpacking operator (**).
Note that the iterable object we’ll get using the unpacking operator ** is 'a dictionary'.
"""

## Concept: Ordering Arguments in a Function

"""
*args must come before **kwargs. The correct order for your parameters is:

    1. Standard arguments
    2. *args arguments
    3. **kwargs arguments
if we try to modify the order of the arguments, we'll recieve an error
"""

# For example, this function definition is correct:
def my_function(a, b, *args, **kwargs):
    pass

## Concept: Unpacking With the Asterisk Operators: * & **

# Unpacking a list with * operator

""" The single asterisk operator * can be used on any iterable that Python provides, 
while the double asterisk operator ** can only be used on dictionaries."""

"""A simple list"""
my_list = [1, 2, 3]
print(my_list) # output: [1, 2, 3]

"""Now let's prepend the unpacking operator * to the name of your list"""
my_list = [1, 2, 3]
print(*my_list) # output: 1, 2, 3

"""
In this case, the output is no longer the list itself, but rather the content of the list
The difference between this execution and the former one is - instead of a list, print() has taken three separate arguments as the input.
Another thing to notice is - we used the unpacking operator * to call a function, instead of in a function definition. In this case, print() takes all the items of a list as if they were single arguments.
"""

# Using * operator in function call

"""We can also use this method to call our own functions, but if our function requires a specific number of arguments, then the iterable we unpack must have the same number of arguments."""
def my_sum(a, b, c):
    print(a + b + c)

my_list = [1, 2, 3]
my_sum(*my_list) # output: 6

"""In this example my_sum() still expects just three arguments, but the * operator gets 4 items from the list."""
# def my_sum(a, b, c):
#     print(a + b + c)

# my_list = [1, 2, 3, 4]
# my_sum(*my_list) # output: TypeError: my_sum() takes 3 positional arguments but 4 were given

"""
When we use the * operator to unpack a list and pass arguments to a function, it’s exactly as if we’re passing every single argument alone. 
This means that we can use multiple unpacking operators to get values from several lists and pass them all to a single function.
"""

"""consider the following example"""
def my_sum(*args):
    result = 0
    for x in args:
        result += x
    return result

list1 = [1, 2, 3]
list2 = [4, 5]
list3 = [6, 7, 8, 9]

print(my_sum(*list1, *list2, *list3)) # output: 45 (Here all three lists are unpacked. Each individual item is passed to my_sum(), resulting in the output)

# Splitting a list with * operator
"""
Say we need to split a list into three different parts. 
The output should show the first value, the last value, and all the values in between. 
Here, In the below example, my_list contains 6 items. The first variable is assigned to a, the last to c, and all other values are packed into a new list b.
"""
my_list = [1, 2, 3, 4, 5, 6]
a, *b, c = my_list
print(a) # output: 1
print(b) # output: [2, 3, 4, 5]
print(c) # output: 6

# Merging multiple lists with * operator:
first_list = [1, 2, 3]
second_list = [4, 5, 6]
third_list = [7, 8, 9]
merged_list = [*first_list, *second_list, *third_list]
print(merged_list) # output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Unpack a string with the * operator
a = [*"Python"]
print(a) # output: ['P', 'y', 't', 'h', 'o', 'n']

# Merging multiple dictionaries by using the unpacking operator **
first_dict = {"A": 1, "B": 2}
second_dict = {"C": 3, "D": 4}
third_dict = {"E": 3, "F": 4}
merged_dict = {**first_dict, **second_dict, **third_dict}
print(merged_dict) # output: {'A': 1, 'B': 2, 'C': 3, 'D': 4}

# Using ** to turn a dictionary into a series of keyword arguments.
movie = {
	"title": "The Matrix",
	"director": "Wachowski",
	"year": 1999
}

def movie_info(**kwargs):
    for key, value in movie.items():
        print(f"{key} : {value}")

movie_info(**movie)

# [ln 1] title: The Matrix
# [ln 2] director: Wachowski
# [ln 3] year: 1999

"""
Here when we do **movie when calling the function, it turns the dictionary into keyword arguments. 
These are passed to print_movie, and the **kwargs parameter collects them back into a dictionary.
"""

"""We could just as well do the following. It would give us the same result."""
def print_movie(movie_details):
	for key, value in movie_details.items():
		print(f"{key}: {value}")

print_movie(movie)

"""
However, **kwargs can give us more flexibility when it comes to collecting unassigned keyword arguments, and not only those coming from a dictionary.
"""
""" For example we can use a custom arguments along with a dictionary"""
def print_movie(**kwargs):
	for key, value in kwargs.items():
		print(f"{key}: {value}")

print_movie(studio="Warner Bros", **movie)

# [ln 1] studio: Warner Bros
# [ln 2] title: The Matrix
# [ln 3] director: Wachowski
# [ln 4] year: 1999


## Exercise:

#1. Create a function that accepts any number of numbers as positional arguments and prints the sum of those numbers. Remember that we can use the sum function to add the values in an iterable.
def multi_add(*numbers):
	print(sum(numbers))
multi_add(1,3,4) # output: 8

#2. Create a function that accepts any number of positional and keyword arguments, and that prints them back to the user. Your output should indicate which values were provided as positional arguments, and which were provided as keyword arguments.
def arg_printer(*args, **kwargs):
	print(f"Positional arguments are: {args}")
	print(f"Keyword arguments are: {kwargs}")
arg_printer(1,  "blue",  [1,  23,  3], height=184, key=lambda x: x ** 2)
# [ln 1]: Positional arguments are: (1, 'blue', [1, 23, 3])
# [ln 2]: Keyword arguments are: {'height': 184, 'key': <function <lambda> at 0x0000024673F77B70>}

#3. Print the following dictionary using the format method and ** unpacking.
country = {
 	"name": "Germany",
 	"population": "83 million",
 	"capital": "Berlin",
 	"currency": "Euro"
}

def country_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

country_info(**country)

#4. Using * unpacking and range, print the numbers 1 to 20, separated by commas.
print(*range(1,21), sep=", ")

#5. Modify your code from exercise 4 so that each number prints on a different line. You can only use a single print call.
print(*range(1,21), sep="\n")