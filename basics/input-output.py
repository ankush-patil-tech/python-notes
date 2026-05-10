"""
=====================================================
INPUT AND OUTPUT IN PYTHON
=====================================================

Input:
Used to take data from user.

Output:
Used to display data.
"""

# ==========================
# PRINT FUNCTION
# ==========================
print("Hello World")

name = "Ankush"
age = 24

print(name)
print(age)

# ==========================
# MULTIPLE VALUES
# ==========================
print("Name:", name, "Age:", age)

# ==========================
# SEPARATOR
# ==========================
print(1, 2, 3, sep="-")

# ==========================
# END PARAMETER
# ==========================
print("Hello", end=" ")
print("World")

# ==========================
# USER INPUT
# ==========================
# input() always returns string

user_name = input("Enter your name: ")
print("Welcome", user_name)

# ==========================
# INTEGER INPUT
# ==========================
age = int(input("Enter age: "))
print("Age is", age)

# ==========================
# FLOAT INPUT
# ==========================
height = float(input("Enter height: "))
print(height)

# ==========================
# FORMATTED STRINGS
# ==========================
name = "Ankush"
course = "Python"

print(f"My name is {name} and I am learning {course}")

# ==========================
# OLD STYLE FORMATTING
# ==========================
print("My name is {}".format(name))

# ==========================
# ESCAPE CHARACTERS
# ==========================
print("Hello\nWorld")
print("Hello\tWorld")

# ==========================
# MULTILINE STRING
# ==========================
message = """
This is line 1
This is line 2
This is line 3
"""

print(message)