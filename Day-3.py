# Day 3: Formatting Strings and Processing User Input

# Concept: String concatenation

""" In Python, we can just use the + operator for String concatenation """
name = "John"
greet = "Hello "
print(greet+name)

# Concept: Converting strings, integers, and floats

""" str(), int(), float() methods are used to convert other types to strings, integers, and floats

# Concept: String interpolation with f-strings
name = "John"
age = 8
detail = f"{name} is {age*2} years old"
print(detail)
# output: John is 16 years old

# Concept: Basic String Processing
print("hello world".lower())
print("hello world".upper())
print("hello world".capitalize())
print("hello world".title())

# strip() - removes extraneous white space
print("  Hello, World!  ".strip())

#1. Using the variable below, print "Hello, world!".
greeting = "Hello, world{}"
print(greeting.format("!"))

#2. Ask the user for their name, and then greet the user, using their name as part of the greeting. The name should be in title case, and shouldn't be surrounded by any excess white space.
name = input("Enter your name: ")
greet = f"Hello, {name}!"
print(greet.title())

#3. Concatenate the string "I am " and the integer 29 to produce a string which reads "I am 29".
print("I am " + str(29))

#4. Format and print the information below using string interpolation.
title = "Joker"
director = "Todd Phillips"
release_year = 2019

film = "{0} ({2}), directed by {1}".format(title, director, release_year)
print(film)

# Project: A Simple Earnings Calculator
employee_name = input("Name of employee: ")
hourly_wage = int(input("Hourly wage: "))
hours_worked = int(input("Working hours: "))
detail = f"{employee_name.title()} earned ${hourly_wage*hours_worked} this week."
print(detail.strip())









