# file handling

# === read a file ===

# must be existing file
# f = open("abc.txt", "r")

# content = f.read()  # read whole file and return as a single string
# content = (
#     f.readlines()
# )  # read whole and return as a list of lines, list splitting by line break
# content = f.read()
# content.replace("**userName**", "Basit Ahmed")
# print(content)


# f = open("abc.txt", "r")

# for a in f.readlines():
#     print(a)


# === write file ===
# if file doesn't exist it will create

# f = open("test.txt", "w")

# it will write file and overwrite text by new text
# f.write("ABC")

# it will write in file line by line but you have to put \n in exery index.
# f.writelines(["ABC\n", "EFG\n", "HIJ\n", "KLM\n"]) #


# f = open("test.txt", "a")
# f.write("ABC\n")


# f.read()  # Error because it calls for append not read


# === read and write ===


# f = open("abc.txt", "w")
# f.write("ABC")
# f.close()

# ff = open("abc.txt", "r")
# content = ff.read()
# ff.close()

# print(content)


# f = open("abc.txt", "")

# "r+" # read and write but base operator is read
# "w+" # write and read but base operator is write
# "a+" # append and read but base operator is append

# when one operation is invoked pointer sets on the last and second read operation give empty because after that pointer there is nothing to read. if we set pointer to start after one operation we can read file after pointer marks.

# f.seek(0)
# this code will set the pointer at 0 position and after that i can read.


# f = open("abc.txt", "w+")
# f.write("ACBDEFGHIJKL")
# content = f.read()
# print(content)

# is is giving empty because pointer settled at the end but if write like

# f = open("abc.txt", "w+")
# f.write("ACBDEFGHIJKL")
# f.seek(0)
# content = f.read()
# print(content)

# it will give complete file

# if you want to find the pointer position;

# pointer_position = f.tell()

# it will give the position where pointer actually is

# import time

# f = open("abc.txt", "w")
# for a in range(1, 60):
#     f.write("Line " + str(a) + "\n")
#     if a % 10 == 0:
#         f.flush()
#         f.write(str(a) + " times Done" + "\n")
#         print(a)
#         print("Flush")
#     time.sleep(1)

# line No: 89 = Import time module which is built in python.
# line No: 91 = file Overwrite only on this line.
# line No: 93 = not on this line
# line No: 94 = check condition for 10 times
# line No: 95 = empty python memory and send data to the file
# line No: 99 = it will delay the programming for seconds which is givin in sleep perameter


# import os

# current_working_directory = os.getcwd()
# files_dir_in_list = os.listdir()
# path = os.path.join("folder_1", "xyz.txt")
# f = open("folder_1/xyz.txt", "a")
# f.write("XYZ")
# print(files_dir_in_list)

# {{Tasks}}

# f = open("abc.txt", "r")
# content = f.read()
# content = content.replace("**userName**", "Basit Ahmed")
# content = content.replace("**fatherName**", "Ayaz Ahmed")
# content = content.replace("**age**", "18")
# print(content)


# content = f.readlines()
# for row in content:
#     print(row)


# row = f.readline()
# print("row ==>", row)


# f = open("abcd.txt", "w")
# f.write("ABC")


# f = open("abc.txt", "a+")
# f.seek(0)
# f.write("123456789")
# f.seek(0)
# content = f.read()

# print(content)

import os

current_dir = os.getcwd()
parent = os.path.join(current_dir, "..")
print(parent)
ab = os.path.abspath(parent)
parent_folder = os.listdir(ab)
print(parent_folder)

for a in parent_folder:
    pth = os.path.join(ab, a)
    print(pth)
