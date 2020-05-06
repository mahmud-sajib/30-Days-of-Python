## Day 9: Unpacking, Enumeration, and the zip Function

## Concept: Unpacking

# With unpacking we no longer have to aceess tuple values with indices, we can use arguments/variables instead.

# a simple tuple
movie = ("Memento", "Christopher Nolan", 2000)
# assigining tuple values to variables 
title, director, year = movie
# printing tuple values
print(title) # output: Memento

# Unpacking in for loops
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

for title, director, year in movies:
    print(f"{title} ({year}) by {director}")

# [ln1]: Eternal Sunshine of the Spotless Mind (2004) by Michel Gondry
# [ln2]: Memento (2000) by Christopher Nolan
# [ln3]: Requiem for a Dream (2000) by Darren Aronofsky

## Concept: Enumerate

# enumerate is a built in function that generates a counter alongside the values in an iterable
names = ["Harry", "Rachel", "Brian"]
for counter, name in enumerate(names):
    print(f"{counter}. {name}")

# [ln1]: 0. Harry
# [ln2]: 1. Rachel
# [ln3]: 2. Brian

# we can set a starting value for the counter when we call enumerate
names = ["Harry", "Rachel", "Brian"]
for counter, name in enumerate(names, start=1):
    print(f"{counter}. {name}")

# [ln1]: 1. Harry
# [ln2]: 2. Rachel
# [ln3]: 3. Brian

# unpacking & enumerate together to print a nice movie list
for counter, (title, director, year) in enumerate(movies, start=1):
	print(f"{counter}. {title} ({year}), by {director}")

# [ln1]: 1. Eternal Sunshine of the Spotless Mind (2004), by Michel Gondry
# [ln2]: 2. Memento (2000), by Christopher Nolan
# [ln3]: 3. Requiem for a Dream (2000), by Darren Aronofsky

## Concept: The zip function

# zip is an extremely powerful and versatile function used to combined two or more iterables into a single iterable.
pet_owners = ["Paul", "Andrea", "Marta"]
pets = ["Fluffy", "Bubbles", "Captain Catsworth"]
pets_and_owners = zip(pet_owners, pets)
print(list(pets_and_owners))
# output: [('Paul', 'Fluffy'), ('Andrea', 'Bubbles'), ('Marta', 'Captain Catsworth')]

# Using zip in loops
pet_owners = ["Paul", "Andrea", "Marta"]
pets = ["Fluffy", "Bubbles", "Captain Catsworth"]

for owner, pet in zip(pet_owners, pets):
    print(f"{owner} owns {pet}")

# [ln1]: Paul owns Fluffy
# [ln2]: Andrea owns Bubbles
# [ln3]: Marta owns Captain Catsworth

## Concept: A caveat for when using enumerate and zip

# To avoid having empty values from enumerate/zip function convert them into list/tuple
movie_titles = [
	"Forrest Gump",
	"Howl's Moving Castle",
	"No Country for Old Men"
]

movie_directors = [
	"Robert Zemeckis",
	"Hayao Miyazaki",
	"Joel and Ethan Coen"
]

movies = list(zip(movie_titles, movie_directors))

for title, director in movies:
	print(f"{title} by {director}.")

movies_list = list(movies)
print(f"There are {len(movies_list)} movies in the collection.")
print(f"These are our movies: {movies_list}.")

## Exercise

#1. Below is some simple data about characters from BoJack Horseman. Write a for loop that uses destructuring so that you can print each tuple
main_characters = [
    ("BoJack Horseman", "Will Arnett", "Horse"),
    ("Princess Carolyn", "Amy Sedaris", "Cat"),
    ("Diane Nguyen", "Alison Brie", "Human"),
    ("Mr. Peanutbutter", "Paul F. Tompkins", "Dog"),
    ("Todd Chavez", "Aaron Paul", "Human")
]

for character, actor, species in main_characters:
    print(f"{character} is a {species.lower()} voiced by {actor}.")

#2. Unpack the following tuple into 4 variables.
info = ("John Smith", 11743, ("Computer Science", "Mathematics"))
s_name, s_id, s_detail = info
dept, course = s_detail

#3. Investigate what happens when you try to zip two iterables of different lengths.
owner = ['John', 'Bob', 'Roby', 'Mithila']
pet = ('Tommy', 'Catto', 'Jimmy')
pet_owner = zip(owner, pet)
print(list(pet_owner))
# output: [('John', 'Tommy'), ('Bob', 'Catto'), ('Roby', 'Jimmy')]

## Project: Credit Card Validator

card_number = list(input("Please enter a card number: ").strip())

# Remove the last digit from the card number
check_digit = card_number.pop()

# Reverse the order of the remaining numbers
reverse_card_num = []
i = len(card_number)

while i > 0:
    reverse_card_num.append(card_number[i-1])
    i = i-1

print(reverse_card_num)

# double the even no. positioned digits
processed_digits = []
index = 0

for index, digit in enumerate(reverse_card_num):
    if index % 2 == 0:
        digit = int(digit) * 2
        if digit > 9:
            digit = digit - 9
    processed_digits.append(digit)


processed_digits.append(check_digit)
print(processed_digits)

# sum all the digits of the list
total = 0
for n in processed_digits:
    total = total + int(n)

print(total)

# check validity
if total % 10 == 0:
    print("Valid card")
else:
    print("Invalid card")



















