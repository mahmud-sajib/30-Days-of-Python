## Day 14: Working with Files

## Concept: The open function - By default, open is going to open our files in read mode, which is why we only have read access.

# open() - is used to access a file. We use read() to see the file's content.
my_file = open('example.txt')
print(my_file.read())

# close() - is used to close a file. It's always good to close a file.
my_file.close()

# we can use string "r" to deonote read mode explicitly
my_file = open('example.txt','r')
print(my_file.read())
my_file.close()

# we can use string "w" to deonote write mode. Python is going to create the file for us if it doesn't already exist.
write_file = open("write_example.txt", "w")
write_file.close()

# write() - is used to write information to a file
write_file = open("write_example.txt", "w")
write_file.write("Welcome to the world of python, write_example.txt!")
write_file.close()

# we can use string "a" to deonote append mode. Append mode lets us extend the file's contents.
write_file = open("write_example.txt", "a")
write_file.write("\nNow you have two lines! You're growing up so fast!")
write_file.close()

## Concept: Context managers for working with files -'with' keyword indicates to Python we're using a context manager. 'as' works as variable.

# writing into a file with context managers
with open("another_example.txt", "w") as write_file:
	write_file.write("Welcome to the world, write_example.txt!")

with open("another_example.txt", "a") as append_file:
    append_file.write("\nHolla appending something!")

## Concept: CSV data

# Getting the data out of the file
with open("iris.csv", "r") as iris_file:
    # Splitting the data into rows using readlines()
    iris_data = iris_file.readlines()
print(iris_data)

irises = []
# Creating our new list and trimming off the header row
for row in iris_data[1:]:
    # Creating a dictionary from each row
    sepal_length, sepal_width, petal_length, petal_width, species = row.strip().split(",")
    iris_dict = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width,
        "species": species
    }
    print(iris_dict)
    irises.append(iris_dict)

print(irises)

## Concept: CSV data processing Using the dict function - dict() is an alternative method for creating a dictionary
# Getting the data out of the file
with open("iris.csv", "r") as iris_file:
    # Splitting the data into rows using readlines()
    iris_data = iris_file.readlines()
headers = iris_data[0].strip().split(",")
irises = []
# print(headers)

for row in iris_data[1:]:
    iris = row.strip().split(",")
    iris_dict = dict(zip(headers,iris))
    irises.append(iris_dict)

print(irises)

# Exercise: 

#1. Rewrite the following piece of code using a context manager.
with open("hello_world.txt", "w") as hello:
    hello.write("Hello, World!")

#2. Use append mode to write "How are you?" on the second line of the hello_world.txt file above.
with open("hello_world.txt", "a") as hello:
    hello.write("\nHow are you?")

#3. 
irises = [
	{'sepal_length': '5.1', 'sepal_width': '3.5', 'petal_length': '1.4', 'petal_width': '0.2', 'species': 'Iris-setosa'},
	{'sepal_length': '4.9', 'sepal_width': '3',   'petal_length': '1.4', 'petal_width': '0.2', 'species': 'Iris-setosa'},
	{'sepal_length': '4.7', 'sepal_width': '3.2', 'petal_length': '1.3', 'petal_width': '0.2', 'species': 'Iris-setosa'},
	{'sepal_length': '4.6', 'sepal_width': '3.1', 'petal_length': '1.5', 'petal_width': '0.2', 'species': 'Iris-setosa'},
	{'sepal_length': '5',   'sepal_width': '3.6', 'petal_length': '1.4', 'petal_width': '0.2', 'species': 'Iris-setosa'},
	{'sepal_length': '7',   'sepal_width': '3.2', 'petal_length': '4.7', 'petal_width': '1.4', 'species': 'Iris-versicolor'},
	{'sepal_length': '6.4', 'sepal_width': '3.2', 'petal_length': '4.5', 'petal_width': '1.5', 'species': 'Iris-versicolor'},
	{'sepal_length': '6.9', 'sepal_width': '3.1', 'petal_length': '4.9', 'petal_width': '1.5', 'species': 'Iris-versicolor'},
	{'sepal_length': '5.5', 'sepal_width': '2.3', 'petal_length': '4',   'petal_width': '1.3', 'species': 'Iris-versicolor'},
	{'sepal_length': '6.5', 'sepal_width': '2.8', 'petal_length': '4.6', 'petal_width': '1.5', 'species': 'Iris-versicolor'},
	{'sepal_length': '6.3', 'sepal_width': '3.3', 'petal_length': '6',   'petal_width': '2.5', 'species': 'Iris-virginica'},
	{'sepal_length': '5.8', 'sepal_width': '2.7', 'petal_length': '5.1', 'petal_width': '1.9', 'species': 'Iris-virginica'},
	{'sepal_length': '7.1', 'sepal_width': '3',   'petal_length': '5.9', 'petal_width': '2.1', 'species': 'Iris-virginica'},
	{'sepal_length': '6.3', 'sepal_width': '2.9', 'petal_length': '5.6', 'petal_width': '1.8', 'species': 'Iris-virginica'},
	{'sepal_length': '6.5', 'sepal_width': '3',   'petal_length': '5.8', 'petal_width': '2.2', 'species': 'Iris-virginica'}
]

iris_data = []
i = 0
for i in range(len(irises)):
    iris_list = []
    for value in irises[i].values():
        
        iris_list.append(value)
        print(iris_list)
    x = ",".join(iris_list)
    print(x)
        
    iris_data.append(x)

print(iris_data)
    
for _ in iris_data:
    with open("new.csv", "w") as iris_file:
        iris_file.writelines("sepal_length,sepal_width,petal_length,petal_width,species")
        # Splitting the data into rows using readlines()
        count = 0
        for count in range(len(iris_data)):
            iris_file.writelines("\n")
            iris_file.writelines(iris_data[count])
            iris_file.writelines("\n")
            count += 1

# alternative solution
with open("iris_2.csv", "w") as iris_file:
    iris_file.write("sepal_length,sepal_width,petal_length,petal_width,species" + "\n")
    for iris in irises:
        iris_file.write(",".join(iris.values()) + "\n")

## Project: Reading List (Hard Version)
selected_option = input("Please press 'a' to add books, 'l' to list the books, 'm' to search a book, 'd' to delete a book 'c' to check if a book is read & q to quit: ")

def add_book():
    title = input("Please add book title: ")
    author = input("Please add author name: ")
    pub_year = input("Please add publication year: ")
    is_read = input("Is it read? write yes or no: ")

    with open("book_listing.csv","a") as book_list:
        book_list.write(f"{title},{author},{pub_year},{is_read} \n")

def list_book():
    books = []
    with open("book_listing.csv","r") as reading_list:
        for book in reading_list:
            title, author, pub_year, is_read = book.strip().split(",")
            book_info = {
                'title':title,
                'author':author,
                'pub_year':pub_year,
                'is_read':is_read
            }
            books.append(book_info)
        
    return books

def show_book(show_book_list):
    for book in show_book_list:
        print(f"\n {book['title']}, by {book['author']} ({book['pub_year']}) - {book['is_read']} \n")
    

def find_book():
    reading_list = list_book()
    matching_books = []
    search_term = input("Please enter a book title: ").strip().lower()
    for book in reading_list:
        if search_term in book["title"].lower():
            matching_books.append(book)
    
    return matching_books

def delete_book():
    books = list_book()
    matching_books = find_book()

    if matching_books:
        books.remove(matching_books[0])
        with open("book_listing.csv","w") as book_list:
            for book in books:
                book_list.write(f"{book['title']},{book['author']},{book['pub_year']},{book['is_read']} \n")
    else:
        print("Sorry, we didn't find any books matching that title.")

def mark_as_read():
    books = list_book()
    matching_books = find_book()

    if matching_books:
        index = books.index(matching_books[0])
        books[index]['is_read'] = "yes"
        
        with open("book_listing.csv","w") as book_list:
            for book in books:
                book_list.write(f"{book['title']},{book['author']},{book['pub_year']},{book['is_read']} \n")
    else:
        print("Sorry, we didn't find any books matching that title.")




            

while selected_option != 'q':
    if selected_option == 'a':
        add_book()
    elif selected_option == 'l':
        list_book()
    elif selected_option == 's':
        show_book_list = list_book()
        if show_book_list:
            show_book(show_book_list)
        else:
            print("The list is empty")
    elif selected_option == 'm':
        matching_books = find_book()
        if matching_books:
            show_book(matching_books)
        else:
            print("The list is empty")
    elif selected_option == 'd':
        delete_book()
    elif selected_option == 'c':
        mark_as_read()
    else:
        print("Invalid options")

    selected_option = input("Please press 'a' to add books, 'l' to list the books, 's' to search a book, 'd' to delete a book 'c' to check if a book is read & q to quit: ")




 






