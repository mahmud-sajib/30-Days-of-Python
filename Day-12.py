## Day 12: Functions

## Concept: Why use functions?

"""
A couple of major benefit of using functions:
    1.They allow us to cut down on repeating potentially long and complicated code for operations we want to perform multiple times.
    2.They make our code more readable. It’s much easier to understand print("Hello, world!"), than the lengthy implementation of the print function.    
"""

## Concept: Defining our first function

# A simple function
def get_even_numbers():
	for number in range(1, 11):
		print(number * 2)

get_even_numbers()

## Concept: Function parameters and arguments
def get_even_numbers(amount):
	for number in range(1, amount + 1):
		print(number * 2)

get_even_numbers(5)

## Concept: Specifying multiple parameters
def sayHello(arg, quantity):
	for _ in range(quantity):
		print(arg)

sayHello("Hello", 5)

## Concept: Keyword arguments
def sayHello(arg, quantity):
	for _ in range(quantity):
		print(arg)

sayHello(arg="Hello", quantity=5)

## Exercises

#1. Define four functions: add, subtract, divide, and multiply.
x = int(input("Write first number: "))
y = int(input("Write second number: "))

def add(x,y):
	print(x+y)

def subtract(x,y):
	print(x-y)

def multiply(x,y):
	print(x*y)

def division(x,y):
	if y==0:
		print("Second number can't be 0")
	else:
		print(x/y)

add(x,y)
subtract(x,y)
multiply(x,y)
division(x,y)

#2. Define a function called print_show_info that has a single parameter. The argument passed to it will be a dictionary with some information about a T.V. show. The print_show_info function should print the information stored in the dictionary, in a nice way.
tv_show = {
 	"title": "Breaking Bad",
 	"seasons": 5,
 	"initial_release": 2008
}

def print_show_info(tv_show):
	print(f"{tv_show['title']} ({tv_show['seasons']}) - {tv_show['initial_release']}")
 
print_show_info(tv_show)

#3. Below you’ll find a list containing details about multiple TV series. Use your function, print_show_info, and a for loop, to iterate over the series list, and call your function once for each iteration, passing in each dictionary.
series = [
 	{"title": "Breaking Bad", "seasons": 5, "initial_release": 2008},
 	{"title": "Fargo", "seasons": 4, "initial_release": 2014},
 	{"title": "Firefly", "seasons": 1, "initial_release": 2002},
 	{"title": "Rick and Morty", "seasons": 4, "initial_release": 2013},
 	{"title": "True Detective", "seasons": 3, "initial_release": 2014},
 	{"title": "Westworld", "seasons": 3, "initial_release": 2016},
]

i = 0
def show(series):
	for i in range(len(series)):
		print(f"{series[i]['title']} ({series[i]['initial_release']}) - {series[i]['seasons']} seasons")
		i = i+1
show(series)

#4. Create a function to test if a word is a palindrome.
word = input("Please enter: ")

def palindromeFinder(word):
	word = word.strip().lower()
	word_list = list(word)
	print(word_list)

	word_length = len(word_list)
	print(word_length)
	new_word_list = []

	while word_length-1 >= 0:
		new_word_list.append(word_list[word_length-1])
		word_length -= 1
	print(new_word_list)

	if word_list == new_word_list:
		print("Palindrom")
	else:
		print("Not a Palindrom")

palindromeFinder(word)

## Project: Reading List

reading_list = []
menu_prompt = """Please enter one of the following options:

- 'a' to add a book
- 'l' to list the books
- 'q' to quit

What would you like to do? """

user_option = input(menu_prompt).strip().lower()

def add_book():
	title = input("Title of book: ").strip().title()
	author = input("Author of book: ").strip().title()
	year = input("Publication year: ").strip().title()

	reading_list.append({
		"title":title,
		"author":author,
		"year":year
	})

def display_book():
	for book in reading_list:
		title, author, year = book.values()
		print(f"{title}, by {author} ({year})")


while user_option != 'q':
	if user_option == 'a':
		add_book()
	elif user_option == 'l':
		if reading_list:
			display_book()
		else:
			print("Your reading list is empty.")
		break
	else:
		print("Wrong input")

	user_option = input(menu_prompt).strip().lower()













