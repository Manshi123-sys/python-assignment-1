# ==========================
# Assignment 2
# ==========================

# -------- Part 1 --------
# Student Result

name = input("Enter Student Name: ")
student_class = input("Enter Class: ")

m1 = float(input("Enter marks of Subject 1: "))
m2 = float(input("Enter marks of Subject 2: "))
m3 = float(input("Enter marks of Subject 3: "))
m4 = float(input("Enter marks of Subject 4: "))
m5 = float(input("Enter marks of Subject 5: "))

total = m1 + m2 + m3 + m4 + m5
percentage = (total / 500) * 100

print("\n------ Student Result ------")
print("Name       :", name)
print("Class      :", student_class)
print("Total Marks:", total)
print("Percentage :", percentage, "%")


# -------- Part 2 --------
# String Methods

str1 = input("\nEnter First String: ")
str2 = input("Enter Second String: ")

text = str1 + " " + str2

print("\nConcatenated String:", text)

print("lower()      :", text.lower())
print("upper()      :", text.upper())
print("title()      :", text.title())
print("swapcase()   :", text.swapcase())
print("capitalize() :", text.capitalize())
print("casefold()   :", text.casefold())
print("center(40)   :", text.center(40))
print("count('a')   :", text.count('a'))
print("endswith('a'):", text.endswith('a'))
print("find('a')    :", text.find('a'))
print("isalnum()    :", text.isalnum())
print("isdigit()    :", text.isdigit())
print("isnumeric()  :", text.isnumeric())
print("isspace()    :", text.isspace())
print("replace()    :", text.replace("a", "@"))


# -------- Part 3 --------
# Assignment Operators

num = 20

print("\nAssignment Operators")

print("Initial Value =", num)

num += 5
print("After += 5 :", num)

num -= 3
print("After -= 3 :", num)

num *= 2
print("After *= 2 :", num)

num /= 4
print("After /= 4 :", num)

num //= 2
print("After //= 2 :", num)

num %= 3
print("After %= 3 :", num)

num **= 2
print("After **= 2 :", num)
