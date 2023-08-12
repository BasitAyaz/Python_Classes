# Loop in object

# obj = {"id": 1, "name": "abc"}

# for x in obj:
#     print(x)  # keys
#     print(obj[x])  # values

# obj = [
#     {"id": 2, "name": "ABC"},
#     {"id": 2, "name": "ABC"},
#     {"id": 2, "name": "ABC"},
#     {"id": 2, "name": "ABC"},
# ]

# for x, y in enumerate(obj):  # first Peramater for index and second for value
#     print(x, y)


# obj = {"id": 2, "name": "ABC"}

# for x, y in enumerate(obj):
#     print(x, y)


# loop in string

# a = "abc"

# for x in a:
#     print(x)


# nested loop
# for a in range(1, 11):
#     for b in range(a):
#         print("*", end="")
#     print()


# while loop

# x = 10
# while x > 0:
#     print(x)
#     x -= 1


# user_input = int(input("Enter a number between 1 and 10 \n"))
# while user_input < 0 or user_input > 10:
#     user_input = int(input("Enter a valid Number \n"))
# print(f"Valid Number is {user_input}")


# count = 0
# while count < 20:
#     count += 1
#     print(count)

# l1 = [1, 2, 3, 4, 5, 6]
# while len(l1):
#     l1.pop()
#     print(l1)


# function


# def foo():
#     print("Foo")

# foo()


# peramter

# def abc(a):
#     print(a)

# abc("1244")


# local variable

# def abc():
#     count = 20

# print(count)
# abc()

# return
# def abc():
#     count = 10
#     return count

# ab = abc()
# print(ab)

# default perameter
# def abc(a=10, b=20):
#     print(a * b)


# abc(2, 2)

# keyword argument

# positional argument are required

# def abc(a, b):
#     print(a, b)


# abc(b=10, a=20)

# rest Operator in Python

# def abc(*a):
#     print(list(a))


# abc(1, 2, 3, 4, 5, 6)


l1 = [
    {"id": 1, "name": "abc", "gender": "male"},
    {"id": 2, "name": "xyz", "gender": "male"},
    {"id": 3, "name": "jkl", "gender": "female"},
]


# def findUser():
#     for x in l1:
#         if x["id"] == 1:
#             return x
def findUser(id):
    for x in l1:
        if x["id"] == id:
            return x


def findUserByName(name):
    for x in l1:
        if x["name"].find(name) != -1:
            return x


def findGender(gender):
    l2 = []
    for x in l1:
        if x["gender"] == gender:
            l2.append(x)
    return l2


def findCustomUser(key, val):
    l2 = []
    for x in l1:
        if x[key] == val:
            l2.append(x)
    if len(l2) == 1:
        return l2[0]
    else:
        return l2


user = findUser(3)
user = findUserByName("k")
user = findGender("female")
user = findCustomUser("name", "asd")

print(user)
