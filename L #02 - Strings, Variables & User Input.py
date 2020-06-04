## Day 2: Strings, Variables, and Getting Input from Users

## Concept: String basics

# strings are ordered sequences of one or more characters surrounded by single/double quote
text = "This is a string!"

## Concept: The exception

# When we refer to a variable that is not defined yet, NameError exception occurs
salary
print(salary*2)
# output: NameError: name 'salary' is not defined

## Concept: Getting values from the user

# input() - used to get values from the user
name = input("Please enter your name: ")

## Exercises

#1. Ask the user for their name and age, assign theses values to two variables, and then print them.
name = input("Please enter your name: ")
print(name) # john

age = input("Please enter your age: ")
print(age) # 25

#2. Investigate what happens when you try to assign a value to a variable that you’ve already defined. Try printing the variable before and after you reuse the name.
country = "Oman"
print(country) # Oman
country = "Syria"
print(country) # Syria

#3. Debug & fix the errors
hourly_wage = input("Please enter your hourly wage: ")
print("Hourly wage: ")
print(hourly_wage) # 25
hours_worked = input("How many hours did you work this week? ")
print("Hours worked: ")
print(hours_worked) # 30

