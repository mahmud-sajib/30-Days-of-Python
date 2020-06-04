## Day 8: While Loops

## concept: While Loop

# We need to use the while keyword, followed by some condition to test. If the condition evaluates to a truthy value, the loop will run one iteration, and then it will test the condition again.
user_number = input("Please enter a number: ")
while int(user_number) < 10:
	print("Your number was less than 10.")
	user_number = input("Please select another number: ")

print("Your number was at least 10.")

# Infinite loops - we can use 'break' to stop an infinite loop
while True:
	selected_option = input("Please enter 'a', 'b', or 'c', or enter 'q' to quit: ")
	if selected_option == "a":
		print("You selected option 'a'!")
	elif selected_option == "b":
		print("You selected option 'b'!")
	elif selected_option == "c":
		print("You selected option 'c'!")
	elif selected_option == "q":
		print("You selected option 'q'! Quitting the menu!")
		break
	else:
		print("You selected an invalid option.")

## Concept: The continue keyword

""" While break allows us to exit a loop, continue allows us to skip the current iteration of a loop. """

for number in range(10):
	if number % 2 != 0:
		continue
	print(number) # output: 0 2 4 6 8

## Concept: Using an else clause with loops

# 'else' clause can be used with for loops and while loops too. An else clause attached to a loop will only run if a break statement wasn't encountered during the execution of that loop.
num = int(input("Please input a number: "))
i = 2
while i < num:

	# If user's number is divisible by the curent divisor, break the loop
	if (num % i == 0):
		print(f"{num} is not prime")
		break
	# Increment the divisor for the next iteration
	i = i + 1

# This line only runs if no divisors produced integer results
else:
	print(f"{num} is prime")




## Exercise:

#01. Write a short guessing game program using a while loop.
while True:
	num = int(input("Please guess a number between 1 & 100: "))
	if num > 50:
		print("Too high")
	elif num < 50:
		print("Too low")
	elif num == 50:
		print("Nice guess")
		break
	else:
		print("Invalid input")

#2. Use a loop and the continue keyword to print out every character in the string "Python", except the "o".
word = "Python"
for w in word:
	if w == "o":
		continue
	print(w)

#3. Using one of the examples from earlier—or a solution entirely of your own—create a program that prints out every prime number between 1 and 100.
primes = []
for num in range(2,101):
		for i in range(2,num):
			if (num % i == 0):
				break
		else:
			primes.append(num)

print(primes)
		
		
	
	
	













