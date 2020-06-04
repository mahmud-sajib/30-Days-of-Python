## Day 11: Sets

## Concept: Defining a set - we define sets using curly braces, including a series of comma separated values.

# Set only contain one instance(unique) of any item (we can't add tuples, lists or dictionaries to a set)
vegetables = {"carrot", "lettuce", "broccoli", "onion", "carrot"}
print(vegetables)
# output: {'carrot', 'onion', 'broccoli', 'lettuce'}

## Concept: Modifying sets

# add() - allows us to add a single value to the set
vegetables = {"carrot", "lettuce", "broccoli", "onion"}
vegetables.add("tomato")
print(vegetables)
# output: {'broccoli', 'onion', 'lettuce', 'tomato', 'carrot'}

# update() - allows us to add several value to the set(we can pass in any iterable - tuple/list)
vegetables = {"carrot", "lettuce", "broccoli", "onion"}
vegetables.update(("banana", "mango"))
print(vegetables)
# output: {'mango', 'broccoli', 'onion', 'lettuce', 'banana', 'carrot'}

# remove() - allows us to remove a single item from a set (clear() makes the set empty)
vegetables = {"carrot", "lettuce", "broccoli", "onion"}
vegetables.remove("lettuce")
print(vegetables)
# output: {'onion', 'carrot', 'broccoli'}

## Concept: Set operations

# Union - The union of two sets is essentially the combination of the two sets.
letters = {"a", "b", "c"}
numbers = {1, 2, 3}
letters_and_numbers = letters.union(numbers)
print(letters_and_numbers)
# output: {1, 2, 3, 'b', 'c', 'a'}

# Intersection - When we find the intersection of two sets, we get a new set containing the elements common to both sets.
numbers = {1, 2, 3}
digits = {3, 4, 5}
numbers_and_digits = numbers.intersection(digits)
print(numbers_and_digits)
# output: {3}

# difference - Gives us the unique value of 1st set comparing the value of 1st & 2nd set.
hall_1 = {"Resident Evil 3", "Final Fantasy VII", "Cyberpunk 2077"}
hall_2 = {"Doom Eternal", "Halo Infinite", "Resident Evil 3"}
hall = hall_1.difference(hall_2)
print(hall)
# output: {'Cyberpunk 2077', 'Final Fantasy VII'}

# symmetric_difference - Gives us all the unique value of of both 1st set & 2nd set comparing the values of both sets.
hall = hall_1.symmetric_difference(hall_2)
print(hall)
# output: {'Cyberpunk 2077', 'Halo Infinite', 'Doom Eternal', 'Final Fantasy VII'}

## Concept: Set operations with other collections

# We can pass in any collection to work with Set operation. Python will convert the collection we pass in to a set before performing the operation.
letters = {"a", "b", "c"}
numbers = [1, 2, 3]
letters_and_numbers = letters.union(numbers)
print(letters_and_numbers)
# output: {'a', 2, 1, 3, 'c', 'b'}

## Concept: Checking if items are in collections

# If we want to check wether a value is in a collection or not, we can use 'in' keyword. 'in' will yield True if the item is found, and False otherwise.
numbers = {1, 2, 3, 4, 5}
print(3 in numbers)  # True
print(7 in numbers)  # False

# We can also use in to check if a key/value is in a dictionary,
student = {
	"name": "Eric Cartman",
	"age": 10,
	"school": "South Park Elementary"
}
print("grades" in student)  # False
print(10 in student.values()) # True

## Exercises

#1. Create an empty set and assign it to a variable
letter = set()

#2. Add three items to your empty set using either several add calls, or a single call to update.
letter.update(("b", "c", "a"))
print(letter)

#3. Create a second set which includes at least one common element with the first set.
alphabet = {"e", "f", "c"}

#4. Find the union, symmetric difference, and intersection of the two sets. Print the results of each operation.
u = letter.union(alphabet)
print(u)

d = letter.symmetric_difference(alphabet)
print(d)

i = letter.intersection(alphabet)
print(i)

#5. Create a sequence of numbers using range, then ask the user to enter a number. Inform the user whether or not their number was within the range you specified.
s = set()
for i in range(1, 6):
    s.add(i)
print(s)
user_num = int(input("Please enter a number: "))
print(user_num in s)




