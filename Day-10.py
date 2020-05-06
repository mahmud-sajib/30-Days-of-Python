## Day 10: Dictionaries

## Concept: Dictionary

""" 
Dictionaries are Python's version of something called an associative array arranged in key:value pairs.

Dictionary keys - A key is a little bit like a variable (written as strings, integers, etc.) is that it's a thing which we can use to refer to some value.

Defining a dictionary - When we want to create a dictionary with content, we have to work in pairs of keys and values. 
A dictionary can't have a key without a value, and we can't have a value which isn't associated with a key.
"""

# simple dictionary
student = {
	"name": "John Smith",
	"grades": [88, 76, 92, 85, 69]
}

## Concept: Accessing values in a dictionary

# We can access values in a dictionary using a subscription expression, just like we do for lists and tuples. However, instead of using an index, we retrieve values using their keys.

# accessing values from dictionary
student = {
	"name": "John Smith",
	"grades": [88, 76, 92, 85, 69]
}
print(student["grades"])
# output: [88, 76, 92, 85, 69]

# get() - is used to determine If a key exists
print(student.get("grade")) # output: None

# we can specify a different default value by passing in a second value to get
print(student.get("grade","A")) # output: A

## Concept: Modifying a dictionary

# Adding items to a dictionary
student = {
	"name": "John Smith",
	"grades": [88, 76, 92, 85, 69]
}
student["age"]=17
print(student)
# output: {'name': 'John Smith', 'grades': [88, 76, 92, 85, 69], 'age': 37}

# We can also extend a dictionary using an existing dictionary and the 'update' method.
movie = {
	"title": "Avengers: Endgame",
	"directors": ["Anthony Russo", "Joe Russo"],
	"year": 2019
}
meta_info = {
	"budget": "$356 million",
	"earnings": "$2.798 billion"
}
movie.update(meta_info)
print(movie)
# output: {'title': 'Avengers: Endgame', 'directors': ['Anthony Russo', 'Joe Russo'], 'year': 2019, 'budget': '$356 million', 'earnings': '$2.798 billion'}

## Concept: Modifying existing items in a dictionary

# The approach for modifying items is actually exactly the same as when we want to add new ones. 
student = {
	'name': 'John Smith',
	'age': 15
}
student["age"] = 20

# We can also use the update method to replace many values at once
student.update({
    'school': 'Rifles public'
})
print(student)
# output: {'name': 'John Smith', 'age': 20, 'school': 'Rifles public'}

## Concept: Deleting items from a dictionary

# del - is used to delete a specific key from the dictionary, which will remove the key:value pair.
movie = {
	"title": "Avengers: Endgame",
	"directors": ["Anthony Russo", "Joe Russo"],
	"year": 2019,
	"runtime": 181
}
del movie["runtime"]
print(movie)
# output: {'title': 'Avengers: Endgame', 'directors': ['Anthony Russo', 'Joe Russo'], 'year': 2019}

# pop(arg_key) - used to remove key:value pair of specified key
movie.pop("directors")
print(movie)
# output: {'title': 'Avengers: Endgame', 'year': 2019}

# clear() - is used to empty the dictionary
movie.clear()
print(movie)
# output: {}

## Concept: Iterating over dictionaries

# values() - is used to get an iterable containing the values for each key in a dictionary
movie = {
	"title": "Avengers: Endgame",
	"directors": ["Anthony Russo", "Joe Russo"],
	"year": 2019
}
for value in movie.values():
    print(value)

# [ln1]: Avengers: Endgame
# [ln2]: ['Anthony Russo', 'Joe Russo']
# [ln3]: 2019

# items() -  gives us a series of tuples, where the first item in each tuple is the key, and the second item is the value.
for key, value in movie.items():
    print(f"{key} : {value}")

# [ln1] title : Avengers: Endgame
# [ln2] directors : ['Anthony Russo', 'Joe Russo']
# [ln3] year : 2019

## Exercise

#1. Below is a tuple describing an album. Convert this outer tuple to a dictionary with four keys
album = (
    "The Dark Side of the Moon",
    "Pink Floyd",
    1973,
    (
        "Speak to Me",
        "Breathe",
        "On the Run",
        "Time",
        "The Great Gig in the Sky",
        "Money",
        "Us and Them",
        "Any Colour You Like",
        "Brain Damage",
        "Eclipse"
    )
)
album_dict = {}
album_dict['name'] = album[0]
album_dict['artist'] = album[1]
album_dict['year'] = album[2]
album_dict['tracks'] = album[3]
print(album_dict)

#2. Iterate over the keys and values of the dictionary you create in exercise 1. For each key and value, you should print the name of the key, and then the value alongside it.
for key, value in album_dict.items():
    print(f"{key} : {value}")

#3. Delete the track list and year of release from the dictionary you created. Once you've done this, add a new key to the dictionary to store the date of release. The date of release for The Dark Side of the Moon was March 1st, 1973.
del album_dict['tracks']
del album_dict['year']
album_dict['release_date'] = 'March 1st, 1973'
print(album_dict)
# output: {'name': 'The Dark Side of the Moon', 'artist': 'Pink Floyd', 'release_date': 'March 1st, 1973'

#4. Try to retrieve one of the values you deleted from the dictionary. This should give you a KeyError. Once you've tried this, repeat the step using the get method to prevent the exception being raised.
print(album_dict.get("year","unknown")) # output: unknown
