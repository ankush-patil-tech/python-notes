"""
=====================================================
VARIABLES AND DATA TYPES IN PYTHON
=====================================================

A variable is used to store data in memory.
Python automatically understands the type of data.
This is called Dynamic Typing.

Example:
x = 10
Here:
- x = variable name
- 10 = value stored in memory

Python Data Types:
1. int        -> Integer numbers
2. float      -> Decimal numbers
3. str        -> Text/String
4. bool       -> True/False
5. list       -> Ordered mutable collection
6. tuple      -> Ordered immutable collection
7. set        -> Unordered unique values
8. dict       -> Key-value pairs
9. NoneType   -> Represents absence of value
"""

# ==========================
# INTEGER
# ==========================
age = 25
print("Age:", age)
print(type(age))

# ==========================
# FLOAT
# ==========================
price = 99.99
print("Price:", price)
print(type(price))

# ==========================
# STRING
# ==========================
name = "Ankush"
print("Name:", name)
print(type(name))

# ==========================
# BOOLEAN
# ==========================
is_student = True
print("Is Student:", is_student)
print(type(is_student))

# ==========================
# LIST
# Mutable = can change
# ==========================
fruits = ["apple", "banana", "mango"]
print(fruits)
print(type(fruits))

# Changing list value
fruits.append("orange")
print(fruits)

# ==========================
# TUPLE
# Immutable = cannot change
# ==========================
coordinates = (10, 20)
print(coordinates)
print(type(coordinates))

# ==========================
# SET
# Stores unique values only
# ==========================
numbers = {1, 2, 3, 4, 4, 4}
print(numbers)
print(type(numbers))

# ==========================
# DICTIONARY
# Key-value pair structure
# ==========================
student = {
    "name": "Ankush",
    "age": 24,
    "course": "AI/ML"
}

print(student)
print(type(student))

# Accessing values
print(student["name"])

# ==========================
# NONE TYPE
# ==========================
result = None
print(result)
print(type(result))

# ==========================
# MULTIPLE VARIABLE ASSIGNMENT
# ==========================
x, y, z = 10, 20, 30
print(x, y, z)

# ==========================
# VARIABLE NAMING RULES
# ==========================
# Valid
user_name = "Ankush"
_user = "Admin"
user1 = "Python"

# Invalid examples
# 1user = "wrong"
# user-name = "wrong"
# class = "wrong"

# ==========================
# TYPE CASTING
# Converting one type to another
# ==========================
num = "100"
print(type(num))

converted_num = int(num)
print(converted_num)
print(type(converted_num))

# Float conversion
pi = "3.14"
print(float(pi))

# String conversion
age = 25
print(str(age))

# Boolean conversion
print(bool(1))
print(bool(0))

# ==========================
# MEMORY CONCEPT
# ==========================
# Variables point to memory locations
# Python manages memory automatically

x = 10
y = x

print(id(x))
print(id(y))

# ==========================
# MUTABLE VS IMMUTABLE
# ==========================
# Immutable Types:
# int, float, str, tuple

# Mutable Types:
# list, dict, set

# Example
list1 = [1, 2, 3]
list2 = list1

list2.append(4)

print(list1)
print(list2)

# Both changed because they reference same object