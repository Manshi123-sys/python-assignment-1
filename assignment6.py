# ======================================
# Assignment 6 - Python Functions
# ======================================

# --------------------------------------
# 1. Maximum of Three Numbers
# --------------------------------------
def maximum(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print("1. Maximum =", maximum(10, 25, 18))


# --------------------------------------
# 2. Distinct Elements from List
# --------------------------------------
def distinct_list(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

numbers = [1, 2, 2, 3, 4, 4, 5, 5, 6]
print("2. Distinct List =", distinct_list(numbers))


# --------------------------------------
# 3. Multiply All Numbers in a List
# --------------------------------------
def multiply_list(lst):
    product = 1
    for num in lst:
        product *= num
    return product

print("3. Product =", multiply_list([2, 3, 4, 5]))


# --------------------------------------
# 4. Factorial of a Number
# --------------------------------------
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

print("4. Factorial =", factorial(5))


# --------------------------------------
# 5. Reverse a String
# --------------------------------------
def reverse_string(text):
    return text[::-1]

print("5. Reverse =", reverse_string("Python"))


# --------------------------------------
# 6. Check Number in Range (10-50)
# --------------------------------------
def check_range(num):
    if 10 <= num <= 50:
        return "Number is within the range."
    else:
        return "Number is outside the range."

print("6.", check_range(35))


# --------------------------------------
# 7. Print Even Numbers from List
# --------------------------------------
def print_even(lst):
    print("7. Even Numbers:")
    for num in lst:
        if num % 2 == 0:
            print(num, end=" ")
    print()

print_even([10, 15, 22, 31, 40, 55, 60])


# --------------------------------------
# 8. Check Prime Number
# --------------------------------------
def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

number = 17
if is_prime(number):
    print("8.", number, "is a Prime Number.")
else:
    print("8.", number, "is NOT a Prime Number.")


# --------------------------------------
# 9. Count Upper and Lower Case Letters
# --------------------------------------
def count_case(text):
    upper = 0
    lower = 0

    for ch in text:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1

    print("9. Upper Case Letters =", upper)
    print("   Lower Case Letters =", lower)

count_case("Hello Python World")
