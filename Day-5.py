## Day 5: Conditionals and Booleans

## Concept: Booleans

# We have two Boolean values in Python - True and False
print(5>10) # False
print(5<10) # True

## Concept: Comparison operators

# 'is' and '==' are different things. '==' compares the value whereas 'is' compares memory location
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True
print(a is b)  # False

# id() - finds the memory adrress of a variable 
print(id(a)) # 1747789439624
print(id(b)) # 1747789439688


## Concept: Conditional statements

# Python has 3 Conditional statements - if, elif, else
age = int(input("How old are you? "))
if age >= 18:
	chosen_drink = "Getting wine for you"
else:
	print("Sorry, we can't serve you.")

## Exercises

#1. Try to approximate the behaviour of the is operator using ==. Remember we have the id function for finding the memory address for a given value, and we can compare memory addresses to check for identity.
a = ("Hello", "World")
b = ("Hello", "World")
print(id(a)) # 1835674044296
print(id(b)) # 1835674044296
print(a==b) # True
print(a is b) # True

#2. Try to use the is operator or the id function to investigate the difference.
numbers = [1, 2, 3, 4]
print(id(numbers)) # 1835672232648
new_numbers = numbers + [5]
print(numbers is new_numbers)
numbers = [1, 2, 3, 4]
numbers.append(5) # False
print(id(numbers)) # 1835672232584

#3. Ask the user to enter a number. Tell the user whether the number is positive, negative, or zero.
num = int(input("Enter number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

#4. Write a program to determine whether an employee is owed any overtime. You should ask the user how many hours the employee worked this week, as well as the hourly wage for this employee.
hours_worked = int(input("Total work hours: "))
hourly_wage = float(input("Hourly wage: "))
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_amount = (overtime_hours*hourly_wage)*(110/100)
    print(f"The employee is due some additional pay which is {overtime_amount:.2f}")
else:
    print("No overtime work done")





