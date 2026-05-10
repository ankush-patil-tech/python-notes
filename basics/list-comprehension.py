"""
=====================================================
LIST COMPREHENSION
=====================================================

List comprehension provides shorter syntax
for creating lists.
"""

# ==========================
# NORMAL METHOD
# ==========================
squares = []

for i in range(5):
    squares.append(i * i)

print(squares)

# ==========================
# LIST COMPREHENSION
# ==========================
squares = [i * i for i in range(5)]
print(squares)

# ==========================
# WITH CONDITION
# ==========================
even_numbers = [i for i in range(10) if i % 2 == 0]
print(even_numbers)

# ==========================
# STRING OPERATIONS
# ==========================
names = ["ankush", "python", "ml"]
uppercase_names = [name.upper() for name in names]
print(uppercase_names)

# ==========================
# NESTED LIST COMPREHENSION
# ==========================
matrix = [[j for j in range(3)] for i in range(3)]
print(matrix)

# ==========================
# DICTIONARY COMPREHENSION
# ==========================
squares_dict = {x: x * x for x in range(5)}
print(squares_dict)

# ==========================
# SET COMPREHENSION
# ==========================
unique_values = {x for x in [1, 2, 2, 3, 3]}
print(unique_values)

# ==========================
# GENERATOR EXPRESSION
# ==========================
generator = (x * x for x in range(5))
print(generator)

for value in generator:
    print(value)

# ==========================
# PERFORMANCE BENEFITS
# ==========================
# List comprehensions are:
# - shorter
# - cleaner
# - often faster than normal loops
