## Day 6: For Loops

## Concept: For loop

# for loop representation
movies = [
	(
		"Eternal Sunshine of the Spotless Mind",
		"Michel Gondry",
		2004
	),
	(
		"Memento",
		"Christopher Nolan",
		2000
	),
	(
		"Requiem for a Dream",
		"Darren Aronofsky",
		2000
	)
]

for movie in movies:
    print(f"{movie[0]} directed by {movie[1]}")

# [ln1]: Eternal Sunshine of the Spotless Mind directed by Michel Gondry
# [ln2]: Memento directed by Christopher Nolan
# [ln3]: Requiem for a Dream directed by Darren Aronofsky

## Concept: The break statement

for movie in movies:
    if movie[0] == "Memento":
        print("It's already listed")
        break
    print(f"{movie[0]} directed by {movie[1]}")

# [ln1]: Eternal Sunshine of the Spotless Mind directed by Michel Gondry
# [ln2]: It's already listed

## Concept: The range function

"""Python has a built in function called range which is capable of producing a series of integers according to some set pattern. 
For example, we might want to get a series of numbers starting from 1 and ending at 100, moving in steps of 3. 
In this case, we'd have 1, 4, 7, 10, 13, 16, 19, etc."""

# range(end) - starts from 0 and ends at specified number
print(range(10)) # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

# using range in for loops - range(initialize,end,steps)
for n in range(1,10,3):
    print(n)
# output: 1, 4, 7

## Exercise

#1. Below we've provided a list of tuples, where each tuple contains details about an employee of a shop: their name, the number of hours worked last week, and their hourly rate. Print how much each employee is due to be paid at the end of the week in a nice, readable format.
employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]
for employee in employees:
    print(f"{employee[0]} will be paid {employee[1]*employee[2]}")

# [ln1]: Rolf Smith will be paid 306.25
# [ln2]: Anne Pun will be paid 375.0
# [ln3]: Charlie Lee will be paid 775.0
# [ln4]: Bob Smith will be paid 140.0

#2. For the employees above, print out those who are earning an hourly wage above average.
total = 0
count = 0
for employee in employees:
    salary = employee[1]*employee[2]
    total = total + salary
    count += 1    

avg = total/count

for employee in employees:
    salary = employee[1]*employee[2]
    if salary > avg:
        print(f"{employee[0]} has salary {salary}")

# output: Charlie Lee has salary 775.0

## Project: Fizz Buzz

for num in range(15):
    num = int(input("Please enter no: "))
    
    if (num % 3 == 0) & (num % 5 == 0):
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        if num > 15:
            print("invalid number")
            break
        else:
            print(num)
    num = num + 1










     
