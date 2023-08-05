# My notes
# '''asdads
# asdasd
# asdasd'''

# (''') like template literals
# ** like spread operator

# all data types in python

# employee = {
#     "name": "ABC",
#     "gender": "male",
#     "dob": "18-May-2023",
#     "address": {"street": "ABC Street", "city": "Karachi", "country": "PK"},
# }
# config = {"company": "HBRM", "Branch": "ABC", "location": "online"}
# countryEnum = {1: "Pakistan", 2: "Turkey", 3: "Bangladesh"}
# print(employee)
# print(employee["address"])
# print(employee["salary"]) # this property doesn't exist program will crash

# print(employee.get("salary")) # this propert doesn't exist but by get() method will return "none" program will not crash

# print(employee.get("salary", "40k")) # if none will come so second perameter value will be replace

# print(employee["address"])
# print(employee["address"]["street"])
# print(employee["address"]["city"])
# print(employee["address"]["country"])
# print(len(employee))
# print(employee)
# employee.update({"name": "XYZ"})
# print(employee)

# changing entity value

# print(employee["dob"])
# employee["dob"] = "aksdkl"
# print(employee["dob"])

# add new value

# employee["salary"] = "50k"
# print(employee)


# delete value

# print(employee)
# del employee["dob"]
# print(employee)

# delet obj
# print(employee)
# employee.clear()
# print(employee)


# object keys and values

# print(employee.keys())
# print(employee.values())

# merge object like spread operator (**) is like spread Operator

# newEmployee = employee | config
# newEmployee = {**employee, **config}
# print(newEmployee)
# print(countryEnum[3])


# Class task

# T:1)create a dictionary named as d1
# d1 = {"name": "Abc", "age": 18, "gender": "Male"}
# print(d1)

# T:2) Update d1 with other properties
# d1.update({"salary": "50k", "department": "IT", "joining_date": "1-Aug-2023"})
# print(d1)

# T:3) delete property age
# del d1["age"]
# print(d1)

# T:4) add new key dob
# d1["dob"] = "18-May-1997"
# print(d1)

# T:5) change the key dob with date_of_birth
# d1["date_of_birth"] = d1["dob"]
# del d1["dob"]
# print(d1)

# T:5) merge d1 with d2

# d2 = {
#     "address": "ABC Street Karachi, Pakistan",
#     "street": "ABC Street",
#     "house_no": "AB-01",
# }


# d3 = {**d1, **d2}
# print(d3)


# for loop
# for loop only works on array like

# for i in ["a", "b", "c", "d"]:
#     print(i)

# x = range(10)
# x = list(x)
# print(x)
# range is a function which creates a squence of Number

# for i in range(10):
#     print(i)
#     print(range(10))

# you can assing itteration negative also
# for i in range(5, 100, 5):
#     print(i)


# continue
# continue us ittration main niche ka code ignore kar k next itration pe jata hai

# break


# for a in range(10):
#     if a == 5:
#         continue
#     print(a)

# this code will not print 5


# for a in range(10):
#     if a == 5:
#         break
#     print(a)
# this code will run 0 to 5 break key word will break the loop

# users = [
#     {"age": 18, "name": "ABC"},
#     {"age": 12, "name": "MNO"},
#     {"age": 10, "name": "JKL"},
#     {"age": 16, "name": "XYZ"},
# ]


# for x in users:
#     print(x)
#     print(x["age"])

# for x in users:
#     if x["name"] == "ABC":
#         print("Present")

# animals = ["cat", "dog", "rabbit", "horse"]

# # get the index of 'dog'
# index = animals.index("dogg")


# print(index)

# # Output: 1

# cold_drinks = ["a", "b", "c"]
# a = "c"

# for x in range(len(cold_drinks)):
#     if cold_drinks[x] == a:
#         print("Available", x)


# for else will work once all itteration done in loop if loops break in mid of all itterations for else will not work

# items = ["a", "b", "c", "d"]
# for a in items:
#     if a == "z":
#         print("Available")
#         break
# else:
#     print("Not Available")
