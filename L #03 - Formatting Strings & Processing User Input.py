## Day 3: Formatting Strings and Processing User Input

## Concept: String concatenation

# We use the '+' operator for string concatenation
name = "John"
greet = "Hello "
print(greet + name)

## Concept: Converting strings, integers, and floats

# str() - convert to string
age = str(28)

# int() - convert to integer
age = int("28")

# float() - convert to float
age = float(28)

## Concept: String interpolation with the format method

# format() -provides a way to insert values within a string 
employee = "{} is {} years old!".format("Rob", 24)
print(employee)
# output: "Rob is 24 years old!"

# Alternatively with format(), we can number placeholders, which will let us reuse values
employee = "{0} is {1} years old, and {0} works as a {2}.".format("John", 24, "web developer")
print(employee)
# output: John is 24 years old, and John works as a web developer.

## Concept: String interpolation with f-strings

# f-strings works in a similar way to format(). We can actually write any expression we want here.
name = "John"
age = 8
detail = f"{name} is {age*2} years old"
print(detail)
# output: John is 16 years old

## Concept: Basic String Processing

# lower() - converts string to lowercase
print("hello world".lower()) # "hello, world!"

# upper() - converts string to uppercase
print("hello world".upper()) # "HELLO, WORLD!"

# capitalize() - converts string to capitalize
print("hello world".capitalize()) # "Hello, world!"

# title() - converts string to title
print("hello world".title()) # "Hello, World!"

# strip() - removes extraneous white space
print("  Hello, World!  ".strip()) # Hello, World!

## Exercises

#1. Using the variable below, print "Hello, world!"
greeting = "Hello, world{}"
print(greeting.format("!"))
# output: Hello, world!

#2. Ask the user for their name, and then greet the user, using their name as part of the greeting. The name should be in title case, and shouldn't be surrounded by any excess white space.
name = input("Enter your name: ")
greet = f"Hello, {name}!"
print(greet.title())
# output: Hello, Ron!

#3. Concatenate the string "I am " and the integer 29 to produce a string which reads "I am 29".
print("I am " + str(29))
# output: I am 29

#4. Format and print the information below using string interpolation.
title = "Joker"
director = "Todd Phillips"
release_year = 2019
film = "{0} ({2}), directed by {1}".format(title, director, release_year)
print(film)
# output: Joker (2019), directed by Todd Phillips

## Project

# A Simple Earnings Calculator
employee_name = input("Name of employee: ")
hourly_wage = int(input("Hourly wage: "))
hours_worked = int(input("Working hours: "))
detail = f"{employee_name.title()} earned ${hourly_wage*hours_worked} this week."
print(detail.strip())
# output: John K earned $150 this week.








