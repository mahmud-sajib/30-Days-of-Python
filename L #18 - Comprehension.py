# ## Day 15: Comprehensions

# ## Concept: List comprehensions - List comprehensions are used to create a new list from some other iterable.

# # List comprehension with list
# names = ["mary", "Richard", "Noah", "KATE"]
# names = [name.title() for name in names]
# print(names)
# # output: ['Mary', 'Richard', 'Noah', 'Kate']

# # List comprehensions with tuples
# names = ("mary", "Richard", "Noah", "KATE")
# ages = (36, 21, 40, 28)
# info = [(name.title(), age) for name, age in zip(names, ages)]
# print(info)
# # output: [('Mary', 36), ('Richard', 21), ('Noah', 40), ('Kate', 28)]

# ## Concept: Set comprehensions - Works like List comprehensions but it produces a set, rather than a list.

# # Set comprehension with list
# names = ["mary", "Richard", "Noah", "KATE"]
# names = {name.title() for name in names}
# print(names)
# # output: {'Richard', 'Mary', 'Kate', 'Noah'}

# ## Concept: Dictionary comprehensions

# # Dictionary comprehension with tuples
# names = ("Mary", "Richard", "Noah", "Kate")
# ages = (36, 21, 40, 28)
# info = {
#     name:age
#     for name, age in zip(names,ages)
# }
# print(info)
# # output: {'Mary': 36, 'Richard': 21, 'Noah': 40, 'Kate': 28}

# ## Concept: Comprehensions and scope

# """
# If we use a comprehension like the following, referring to 'name' gives us a NameError, because 'name' isn't defined.
# """
# names = ["Mary", "Richard", "Noah", "Kate"]
# names_lower = [name.lower() for name in names]
# print(name)  # NameError

# """
# So, what exactly is going on here?
# The reason for these differences is that comprehensions are actually functions. When we write something like this:
# """
# names = ["Mary", "Richard", "Noah", "Kate"]
# names_lower = [name.lower() for name in names]

# """Behind the scenes, Python is running a function similar to this:"""
# def temp():
# 	new_list = []
	
# 	for name in names:
# 		new_list.append(name.lower())

# 	return new_list

# """
# It's just a regular for loop, like we were using before, only this for loop is running inside a function.
# We can now see why the variables inside comprehensions cannot be accessed outside of the comprehension. 
# They only exist while the behind-the-scenes function is running, and they're only available inside that function.
# """"

## Exercises:

#1. Convert the following for loop into a comprehension.
numbers = [1, 2, 3, 4, 5]
numbers = [number**2 for number in numbers]
print(numbers)
# output: [1, 4, 9, 16, 25]

#2. Use a dictionary comprehension to create a new dictionary from the dictionary below, where each of the values is title case.
movie = {
	"title": "thor: ragnarok",
	"director": "taika waititi",
	"producer": "kevin feige",
	"production_company": "marvel studios"
}

movie = {
    key:value.title()
    for key, value in movie.items()
}
print(movie)
# output: {'title': 'Thor: Ragnarok', 'director': 'Taika Waititi', 'producer': 'Kevin Feige', 'production_company': 'Marvel Studios'}