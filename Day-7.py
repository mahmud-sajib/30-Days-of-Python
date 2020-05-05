## Day 7: split, join, and Slices

## Concept: Converting tuples and lists to strings

# join() - takes a list and turn it into string (we can only join list items that have 'str' data type)
authors = ["Mike", "Sofia", "Helen"]
authors = ", " .join(authors)
print("The book is written by " + authors)
# output: The book is written by Mike, Sofia, Helen

## Concept: Splitting up a string

# split() - takes a string and split it into list items
greet = 'I am good. Hope you are too. Go get coffee'.split(".")
print(greet)
# output: ['I am good', ' Hope you are too', ' Go get coffee']

# list() - turns a string into a list
fav_lang = "Python"
print(list(fav_lang))
# output: ['P', 'y', 't', 'h', 'o', 'n']

# tuple() - turns a string into a tuple
fav_lang = "Python"
print(tuple(fav_lang))
# output: ('P', 'y', 't', 'h', 'o', 'n')

## Concept: The newline character

# we represent newline character as \n
print("Super Special Mega \n Awesome Program \n By Phillip Best")
# [ln1]: Super Special Mega
# [ln2]: Awesome Program
# [ln3]:By Phillip Best

## Concept: Slicing

# [0:3] - means we want to start at index 0, and we want to grab every item up to, but not including index 3. It's similar to [:3]
fruit = "Apple"
print(fruit[0:3])
# output: App

# [3:] - means give me everything from index 3 onward
fruit = "Apple"
print(fruit[3:])
# output: le

# [3:-1] - means we want everything from index 3 onward, but not including, the final element.
fruit = "Apple"
print(fruit[3:-1])
# output: l

## Concept: The len function

# len() - used to find how many items are in a given collection
numbers = [1, 2, 3, 4, 5]
print(len(numbers))
# output: 5
text = "Hello World"
print(len(text))
# output: 11

## Exercise:

#1. Ask the user to enter their given name and surname in response to a single prompt. Use split to extract the names, and then assign each name to a different variable. For this exercise, you can assume that the user has a single given name and a single surname.
names = input("Please enter your full name: ").split()
print(names[0])
print(names[1])

#2. Print the list, [1, 2, 3, 4, 5], in the format 1 | 2 | 3 | 4 | 5 using the join method.
num = [1, 2, 3, 4, 5]

str_num = []

for n in num:
   str_num.append(str(n))
print(str_num)

str_num = " | ".join(str_num)
print(str_num)

# output: 1 | 2 | 3 | 4 | 5

#3. Each quote is a string, but each string actually contains quote characters at the start and end. Using slicing, extract the text from each string, without these extra quote marks, and print each quote.
quotes = [
 	"'What a waste my life would be without all the beautiful mistakes I've made.'",
 	"'A bend in the road is not the end of the road... Unless you fail to make the turn.'",
 	"'The very essence of romance is uncertainty.'",
 	"'We are not here to do what has already been done.'"
]

for q in quotes:
    print(q[1:-1])

#ln1: What a waste my life would be without all the beautiful mistakes I've made.
#ln2: A bend in the road is not the end of the road... Unless you fail to make the turn.
#ln3: The very essence of romance is uncertainty.
#ln4: We are not here to do what has already been done.

#4. Ask the user to enter a word, and then print out the length of the word.

# count characters
text = input("Please enter text: ").strip()
char_count = len(text)
print(char_count)

# count words
words = text.split(" ")
print(words)
word_count = 0
for w in words:
    word_count += 1
print(word_count)

## Project: Movie Budgets

movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

num = input("How many movies you want to add: ")
num = int(num)

for n in range(num):
    name = input("Enter new movie name: ")
    budget = int(input("Enter new movie budget: "))
    new_movie = (name, budget)
    
    movies.append(new_movie)
    

print(movies)


total = 0
count = 0
for movie in movies:
    total = total + movie[1]
    count += 1

avg_budget = total/count
print(f"average budget: {avg_budget}")

budget_count = 0
for movie in movies:
    if movie[1] > avg_budget:
        budget_count += 1
        print(f"Movie: {movie[0]} exceeds {movie[1]-avg_budget} than average")
print(budget_count)



