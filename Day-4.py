## Day 4: Basic Python Collections

## Concept: Lists

# list representation
names = ["John", "Alice", "Sarah", "George"]
print(names)
# output: ['John', 'Alice', 'Sarah', 'George']

# Empty list - It’s also possible to define a list with no content, which is represented by an empty pair of square brackets []
names = []

## Concept: Accessing values in a list

# positive index starts with 0 & counts from first to last
names = ["John", "Alice", "Sarah", "George"]
print(names[1])
# output: Alice

# negative index starts with -1 & counts from last to first
print(names[-1])
# output: George

## Concept: Adding items to a list

# append() - adds 1 item into the list 
names = ["John", "Alice", "Sarah", "George"]
names.append("Simon")
print(names)
# output: ['John', 'Alice', 'Sarah', 'George', 'Simon']

# extend() - adds multiple items into the list
names = ['John', 'Alice', 'Sarah', 'George', 'Simon']
names.extend(['Ron', 'Harry'])
print(names)
# output: ['John', 'Alice', 'Sarah', 'George', 'Simon', 'Ron', 'Harry']

# insert() - inserts a value within the list given the index number
numbers = [1, 2, 4, 5]
numbers.insert(2,3)
print(numbers)
# output: [1, 2, 3, 4, 5]

## Concept: Removing items from a list

# remove() -  removes the first item that matches the value we pass in
names = ["John", "Sarah", "Alice", "John"]
names.remove("John")
print(names)
# output: ['Sarah', 'Alice', 'John']

# del - removes the item given the index number
names = ["John", "Sarah", "Alice", "John"]
del names[0]
print(names)
# output: ['Sarah', 'Alice', 'John']

# pop() - removes the last item in the list 
names = ["John", "Sarah", "Alice", "John"]
names.pop()
print(names)
# output: ['John', 'Sarah', 'Alice']

# pop(index) - we can optionally pass in an index as an argument to remove a different item instead
names.pop(0)
print(names)
# output: ['Sarah', 'Alice']

# clear() - removes everything inside a given list & produce an empty list
names = ["John", "Sarah", "Alice", "John"]
names.clear()
print(names)
# output: []

## Concept: Tuples

# tuple representation
names = ("John", "Sarah", "Alice")
print(names)
# output: ('John', 'Sarah', 'Alice')

# tuple concatenation - we can only use '+' to join two tuples
first_names = ("John", "Sarah", "Alice")
last_names = ("Doe", "Ali", "Shefard")
full_names = first_names + last_names
print(full_names)
# output: ('John', 'Sarah', 'Alice', 'Doe', 'Ali', 'Shefard')

## Concept: Accessing values in a tuple

# tuple elements can be accessed by index number same as lists 
names = ("John", "Sarah", "Alice")
print(names[-1])
# output: Alice

## Concept: Tuples vs lists

"""One of big differences between tuples and lists is that tuples are immutable. 
We can’t change them once we define them.
This means you won’t find any pop, del or append methods for tuples."""

## Concept: Accessing values in nested collections

# [] - yields the list element & [][] - yields the tuple value  
movies = [
	("Eternal Sunshine of the Spotless Mind", 2004),
	("Memento", 2000),
	("Requiem for a Dream", 2000)
]
print(movies[1][0])
# output: Memento

## Exercises

#1. Create a movies list containing a single tuple. The tuple should contain a movie title, the director’s name, the release year of the movie, and the movie’s budget.
movies = [
    ("Eternal Sunshine of the Spotless Mind", 
     "Ben Aflick", 
     2004, 
     "1M USD"
    )
]
print(movies)
# output: [('Eternal Sunshine of the Spotless Mind', 'Ben Aflick', 2004, '1M USD')]

#2. Use the input function to gather information about another movie. You need a title, director’s name, release year, and budget.
title = input("Movie title: ")
director = input("Movie director: ")
release_year = input("Release Year: ")
budget = input("Budget: ")

#3. Create a new tuple from the values you gathered using input. Make sure they're in the same order as the tuple you wrote in the movies list.
movie = (title, director, release_year, budget)

#4. Use an f-string to print the movie name and release year by accessing your new movie tuple.
film = f"{movie[0]} {movie[1]} {movie[2]} {movie[3]}"

#5. Add the new movie tuple to the movies collection using append.
movies.append(movie)

#6. Print both movies in the movies collection.
print(movies)
# output: [('Eternal Sunshine of the Spotless Mind', 'Ben Aflick', 2004, '1M USD'), ('Titanic', 'James K.', '2000', '1B USD')]

#7. Remove the first movie from movies. Use any method you like.
del movies[0]
print(movies)
# output: [('Titanic', 'James K.', '2000', '1B USD')]