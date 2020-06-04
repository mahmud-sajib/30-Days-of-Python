## Day 13: Scope and Returning Values from Functions

## Concept: A demonstration of scope

# A variable defined inside a function can only be accessed inside that function
def greet(name):
	greeting = f"Hello, {name}!"
	print(greeting)

greet("Lubu")
# print(greeting) # NameError

## Concept: Namespaces

"""
Python actually keeps a record of the variables we've defined, and the values that are associated with those names. 
We call this record a namespace, and you can think of it as being a dictionary. 
We can get a little peek at this dictionary by calling the globals function and printing the result.

When we use a name in our application, Python just looks in the namespace to see if it's defined. 
If it is, it can just reference the value associated with that name. 
If it can't find the name we requested, Python says that the variable is undefined.
"""

# globals() - returns a dictionary with global namespaces
names = ["Mike", "Fiona", "Patrick"]
x = 53657

def add(a, b):
	print(a, b)

print(globals())

## Concept: Functions and namespaces

# locals() - returns a dictionary with local namespaces(i.e. namespaces inside a function definition)
def add(a, b):
	print(locals()) # {'a': 7, 'b': 25}
	print(a, b)

add(7, 25)

## Concept: Getting values out of a function

# The return statement is used to end the execution of a function. When Python encounters the return keyword, it immediately terminates the function.
def my_func():
	return
	print("This line will never run")

# We can also put an expression directly after the return keyword, and this is how we get values out of the function. We put the values we want to get out on the same line as the return keyword.
def add(a, b):
	return a + b

result = add(5, 12)
print(result)  # 17

# If we don't specify a value to return, Python implicitly returns None for us.
def greet(name):
	greeting = f"Hello, {name}!"

print(greet('Phil')) # None

# we can use the return value of the function anywhere we might use a plain old value. For example, in variable assignment or as part of a string.
def greet(name):
	greeting = f"Hello, {name}!"
	return greeting

print(f"{greet('Phil')}, How are you doing?")
# output: Hello, Phil!, How are you doing?

## Concept: Multiple return statements

# An example of multiple return statements with conditional logic
def divide(a, b):
	if b == 0:
		return "You can't divide by 0!"
	else:
		return a / b
result = divide(10, 0)
print(result)
# output: You can't divide by 0!

## Exercises

#1. Define a exponentiate function that takes in two numbers. The first is the base, and the second is the power to raise the base to. The function should return the result of this operation.
def exponentiate(base, power):
	print(base**power)

exponentiate(5, 2)

#2. Define a process_string function which takes in a string and returns a new string which has been converted to lowercase, and has had any excess whitespace removed.
def process_string(input):
	output = input.strip().lower()
	print(output)

process_string("Holla ")

#3. Write a function that takes in a tuple containing information about an actor and returns this data as a dictionary.
actor = ("Tom Hardy", "English", 42)
def process_tuple(actor):
	name, nationality, age = actor
	return {
		"name": name,
		"nationality": nationality,
		"age": age
	}

output = process_tuple(actor)
print(output)

#4. Write a function that takes in a single number and returns True or False depending on whether or not the number is prime.
num = int(input("Please input a number: "))
def findPrime(num):
	i = 2
	while i < num:
		if num % i  == 0:
			return False
		i+=1
	else:
		return True

output = findPrime(num)
print(output)
















