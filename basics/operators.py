"""
=====================================================
OPERATORS IN PYTHON
=====================================================

Operators are symbols used to perform operations.
"""

# ==========================
# ARITHMETIC OPERATORS
# ==========================
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

# ==========================
# COMPARISON OPERATORS
# ==========================
print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

# ==========================
# LOGICAL OPERATORS
# ==========================
x = True
y = False

print(x and y)
print(x or y)
print(not x)

# ==========================
# ASSIGNMENT OPERATORS
# ==========================
num = 10
num += 5
print(num)

num *= 2
print(num)

# ==========================
# MEMBERSHIP OPERATORS
# ==========================
fruits = ["apple", "banana"]

print("apple" in fruits)
print("mango" not in fruits)

# ==========================
# IDENTITY OPERATORS
# ==========================
a = [1, 2]
b = a
c = [1, 2]

print(a is b)
print(a is c)

# ==========================
# BITWISE OPERATORS
# ==========================
print(5 & 3)
print(5 | 3)
print(5 ^ 3)
print(~5)