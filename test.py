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
