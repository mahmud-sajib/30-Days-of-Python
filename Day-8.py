# ## Day 8: While Loops

# ## concept: While Loop

# while True:
# 	selected_option = input("Please enter 'a', 'b', or 'c', or enter 'q' to quit: ")
	
# 	if selected_option == "a":
# 		print("You selected option 'a'!")
# 	elif selected_option == "b":
# 		print("You selected option 'b'!")
# 	elif selected_option == "c":
# 		print("You selected option 'c'!")
# 	elif selected_option == "q":
# 		print("You selected option 'q'! Quitting the menu!")
# 		break
# 	else:
# 		print("You selected an invalid option.")

# ## Concept: The continue keyword

# """ While break allows us to exit a loop, continue allows us to skip the current iteration of a loop. """

# for number in range(10):
# 	if number % 2 != 0:
# 		continue
# 	print(number)

# ## Concept: Using an else clause with loops

# # Get a number to test from the user, and set the initial divisor to 2
# dividend = int(input("Please enter a number: "))
# divisor = 2

# # Keep looping until the divisor equals the number we're testing
# while divisor < dividend:
# 	# If user's number is divisible by the curent divisor, break the loop
# 	if dividend % divisor == 0:
# 		print(f"{dividend} is not prime!")
# 		break
		
# 	# Increment the divisor for the next iteration
# 	divisor = divisor + 1
# else:
# 	# This line only runs if no divisors produced integer results
# 	print(f"{dividend} is prime!")


## Exercise:

#01.



# while True:
# 	num = int(input("Please guess a number between 1 & 100: "))
# 	if num > 50:
# 		print("Too high")
# 	elif num < 50:
# 		print("Too low")
# 	elif num == 50:
# 		print("Nice guess")
# 		break
# 	else:
# 		print("Invalid input")

#2.

word = "Python"

for w in word:
	if w == "o":
		continue
	print(w)

#3.

primes = []
for num in range(2,101):
		for i in range(2,num):
			
			if (num % i == 0):
				break
				
		else:
			primes.append(num)

print(primes)
		
		
	
	
	













