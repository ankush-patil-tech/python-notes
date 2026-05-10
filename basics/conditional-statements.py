"""
=====================================================
CONDITIONAL STATEMENTS
=====================================================

Conditional statements help programs make decisions.
"""

# ==========================
# IF STATEMENT
# ==========================
age = 18

if age >= 18:
    print("Eligible to vote")

# ==========================
# IF ELSE
# ==========================
num = 5

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# ==========================
# IF ELIF ELSE
# ==========================
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

# ==========================
# NESTED IF
# ==========================
age = 25
salary = 50000

if age > 18:
    if salary > 30000:
        print("Loan Approved")
    else:
        print("Low Salary")
else:
    print("Underage")

# ==========================
# TERNARY OPERATOR
# ==========================
num = 10
result = "Positive" if num > 0 else "Negative"
print(result)

# ==========================
# MATCH CASE (Python 3.10+)
# Similar to switch case
# ==========================

day = 2

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid")