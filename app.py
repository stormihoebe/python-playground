# 1. basic syntax
# 2. reverse a string


def str_reverse(s):
    reversed_str = ""
    for letter in s:
        reversed_str = letter + reversed_str
    return reversed_str


name = "stormi"

print(f"This is your name backwards: {str_reverse(name)}")

# 3. map over a list and convert to something else


def find_total(num_list):
    total = 0
    for num in num_list:
        total += num
    return total


numbers = [3, 5, 7, 9]

print(f"For Loop total: {find_total(numbers)}")

# 4. learn about dictionaries, how to manipulate them, access their keys, iterate etc

# classes


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print("Hello, I'm " + self.name)

    def say_age(self):
        print("I am " + str(self.age) + " years old.")


stormi = Person("Stormi", 27)

stormi.say_hello()
stormi.say_age()

# dictionaries
book = {
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "year": 1925,
    "has_read": True
}

print(f"This book was written by {book['author']}.")
if book["has_read"]:
    print(f'I have read {book["title"]}')
else:
    print(f'I have never read {book["title"]}.')
print(f"This book was written {2020 - book['year']} years ago.")

book["in_stock"] = False

if not book["in_stock"]:
    print(f'{book["title"]} is not in stock.')
else:
    print(f'{book["title"]} is available.')


def check_book_info(book_info):
    book_keys = book_info.keys()
    for key in book_keys:
        print(f"I have info about '{key}'")
        print(f"It's: {book_info[key]}")


check_book_info(book)

# ...
#
# 1. use boto3 to suck down a csv file from AWS and print the contents
# 2. use pandas to join 2 csv files into a single data structure and print that
# 3. create an AWS dynamo db table, access its contents

