# ==============================
# Assignment 4 - Python
# ==============================

# ------------------------------
# 1. List Operations
# ------------------------------
print("===== Question 1 =====")

numbers = [10, 20, 15, 8, 25, 30, 12, 18, 40, 50, 5, 60, 7, 14, 28]

total = sum(numbers)
average = total / len(numbers)
largest = max(numbers)
smallest = min(numbers)

even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("List:", numbers)
print("Total Sum =", total)
print("Average =", average)
print("Largest Number =", largest)
print("Smallest Number =", smallest)
print("Even Numbers =", even)
print("Odd Numbers =", odd)

# ------------------------------
# 2. Access Number 5
# ------------------------------
print("\n===== Question 2 =====")

list_of_lists = [
    [10, 11, 102],
    [1, 2],
    [3, 4, 5],
    [6, 7]
]

print("Number 5 =", list_of_lists[2][2])

# ------------------------------
# 3. Check Value Exists
# ------------------------------
print("\n===== Question 3 =====")

inventory = ["Laptop", "Mouse", "Monitor", "Keyboard"]
target = "Tablet"

if target in inventory:
    print(target, "exists in the inventory.")
else:
    print(target, "does not exist in the inventory.")

# ------------------------------
# 4. Delete Every Instance
# ------------------------------
print("\n===== Question 4 =====")

numbers = [5, 20, 15, 20, 25, 50, 20]
item = 20

while item in numbers:
    numbers.remove(item)

print("Updated List:", numbers)

# ------------------------------
# 5. Create Dictionary
# ------------------------------
print("\n===== Question 5 =====")

keys = ["name", "age", "city"]
values = ["ABC", 25, "Jaipur"]

person = dict(zip(keys, values))

print("Dictionary =", person)

# ------------------------------
# 6. Retrieve Nested Dictionary Value
# ------------------------------
print("\n===== Question 6 =====")

person = {
    "name": "ABC",
    "address": {
        "city": "Jaipur",
        "state": "Rajasthan"
    }
}

print("City =", person["address"]["city"])
