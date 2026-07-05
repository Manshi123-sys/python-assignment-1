# =====================================
# Assignment 5 - Python
# =====================================

# -------------------------------------
# 1. Repeat a tuple three times
# -------------------------------------
print("Question 1")
t1 = (1, 2, 3)
print("Original Tuple:", t1)
print("Repeated Tuple:", t1 * 3)

# -------------------------------------
# 2. Join three tuples
# -------------------------------------
print("\nQuestion 2")
t2 = (4, 5)
t3 = (6, 7)
new_tuple = t1 + t2 + t3
print("Joined Tuple:", new_tuple)

# -------------------------------------
# 3. Check if an element exists in tuple
# -------------------------------------
print("\nQuestion 3")
element = 2

if element in t1:
    print(element, "exists in the tuple.")
else:
    print(element, "does not exist in the tuple.")

# -------------------------------------
# 4. Total, Highest and Lowest
# (without using sum(), max(), min())
# -------------------------------------
print("\nQuestion 4")

numbers = (10, 25, 8, 40, 15)

total = 0
highest = numbers[0]
lowest = numbers[0]

for num in numbers:
    total += num

    if num > highest:
        highest = num

    if num < lowest:
        lowest = num

print("Tuple:", numbers)
print("Total =", total)
print("Highest =", highest)
print("Lowest =", lowest)

# -------------------------------------
# 5. Filter tuple (values > 10)
# -------------------------------------
print("\nQuestion 5")

n = (3, 14, 7, 22, 9, 41, 18, 5)

filtered = ()

for num in n:
    if num > 10:
        filtered += (num,)

print("Filtered Tuple:", filtered)

# -------------------------------------
# 6. Count elements in a set
# (without using len())
# -------------------------------------
print("\nQuestion 6")

s = {"cat", "dog", "bird", "fish"}

count = 0
for item in s:
    count += 1

print("Number of elements:", count)

# -------------------------------------
# 7. Combine two sets
# -------------------------------------
print("\nQuestion 7")

set1 = {1, 2, 3}
set2 = {3, 4, 5}

combined = set1 | set2

print("Combined Set:", combined)

# -------------------------------------
# 8. Common elements in two sets
# -------------------------------------
print("\nQuestion 8")

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

common = s1 & s2

print("Common Elements:", common)

# -------------------------------------
# 9. Elements in either set
# (Symmetric Difference)
# -------------------------------------
print("\nQuestion 9")

either = s1 ^ s2

print("Elements in either set:", either)
