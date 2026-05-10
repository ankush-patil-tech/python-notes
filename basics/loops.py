"""
=====================================================
LOOPS IN PYTHON
=====================================================

Loops are used to repeat code multiple times.

Types:
1. for loop
2. while loop
"""

# ==========================
# FOR LOOP
# ==========================
for i in range(5):
    print(i)

# ==========================
# RANGE FUNCTION
# ==========================
print(list(range(5)))
print(list(range(1, 10)))
print(list(range(1, 10, 2)))

# ==========================
# ITERATING THROUGH LIST
# ==========================
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)

# ==========================
# WHILE LOOP
# ==========================
count = 1

while count <= 5:
    print(count)
    count += 1

# ==========================
# BREAK STATEMENT
# ==========================
for i in range(10):
    if i == 5:
        break
    print(i)

# ==========================
# CONTINUE STATEMENT
# ==========================
for i in range(5):
    if i == 2:
        continue
    print(i)

# ==========================
# PASS STATEMENT
# ==========================
for i in range(3):
    pass

# ==========================
# NESTED LOOPS
# ==========================
for i in range(3):
    for j in range(3):
        print(i, j)

# ==========================
# LOOP ELSE
# ==========================
for i in range(5):
    print(i)
else:
    print("Loop completed")