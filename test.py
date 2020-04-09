# reverse a string
# name = input("What is your name? ")
name = "stormi"
bw = ""
i = 1
while i <= len(name):
    index = i * -1
    bw = bw + name[index]
    i+=1

print(f"While Loop: This is your name backwards: {bw}")

bww = ""
for letter in name:
    bww = letter + bww

print(f"For Loop: This is your name backwards: {bww}")

# add items in a list
total = 0
nums = [4, 7, 8, 20]
for num in nums:
    total += num
print(f"For Loop total: {total}")

# multiply items in a list
nums = [4, 7, 8, 20]
newNums = []
for num in nums:
    newNum = num * 2
    newNums.append(newNum)

print(newNums)

# return largest number in list
nums = [4, 100, 7, 8, 20, 22, -109, 119, 32]
largest_num = nums[0]

for num in nums:
    if num > largest_num:
        largest_num = num
print(largest_num)

matrix = [
    [0, 3, 1],
    [3, 4, 6],
    [3, 1, 4]
]

stormi = {
    "name": "Stormi",
    "age": 27,
    "is_verified": True
}

print(stormi["name"])
print(stormi.get("age"))
print(stormi.get("is_verified"))

def returnPersonName(person):
    return person.get("name")

print("Hello " + returnPersonName(stormi))

the_keys = stormi.keys()
print(the_keys)

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