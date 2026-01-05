"""
==================================================
PYTHON BASICS – PRACTICE FILE
Topics: Variables, Data Types, Operators, Input, Logic
==================================================
"""

# -------------------------------------------------
# 1. VARIABLES AND IDENTIFIERS
# -------------------------------------------------
a = 1
b = 2
c = a + b

name = "Python"
alias = name

print("Hello", alias)
print("Sum of", a, "and", b, "is", c)


# -------------------------------------------------
# 2. DATA TYPES IN PYTHON
# -------------------------------------------------

# Text type
text_value = "Learning Python"
print("Text:", text_value)

# Numeric types
age = 21              # int
height = 5.6          # float
complex_num = 2 + 3j  # complex

print("Age:", age)
print("Height:", height)
print("Complex Number:", complex_num)

# Boolean type
is_active = True
print("Boolean Value:", is_active)

# List and Tuple
fruits_list = ["apple", "banana", "cherry"]
fruits_tuple = ("apple", "banana", "cherry")

print("List:", fruits_list)
print("Tuple:", fruits_tuple)

# Dictionary
info = {"language": "Python", "level": "Beginner"}
print("Dictionary:", info)


# -------------------------------------------------
# 3. OPERATORS IN PYTHON
# -------------------------------------------------
x = 10
y = 3

addition = x + y
subtraction = x - y
multiplication = x * y
division = x / y
modulus = x % y
power = x ** y

print("\nArithmetic Operators:")
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Modulus:", modulus)
print("Exponentiation:", power)


# -------------------------------------------------
# 4. COMPARISON OPERATORS
# -------------------------------------------------
print("\nComparison Operators:")
print("x == y:", x == y)
print("x != y:", x != y)
print("x > y:", x > y)
print("x < y:", x < y)
print("x >= y:", x >= y)
print("x <= y:", x <= y)


# -------------------------------------------------
# 5. ASSIGNMENT OPERATORS
# -------------------------------------------------
value = addition
print("\nAssignment Operators:")
print("Initial value:", value)

value += 5
print("After += 5:", value)

value *= 2
print("After *= 2:", value)

value -= 4
print("After -= 4:", value)


# -------------------------------------------------
# 6. LOGICAL OPERATORS
# -------------------------------------------------
print("\nLogical Operators:")
print("True or False:", True or False)
print("True and False:", True and False)
print("not True:", not True)
print("not False:", not False)


# -------------------------------------------------
# 7. TYPE FUNCTION & TYPE CASTING
# -------------------------------------------------
num = 10
decimal = 5.5
message = "Hello"

print("\nType Function:")
print("Type of num:", type(num))
print("Type of decimal:", type(decimal))
print("Type of message:", type(message))

float_num = float(num)
string_num = str(num)

print("Integer to Float:", float_num)
print("Integer to String:", string_num)


# -------------------------------------------------
# 8. INPUT FUNCTION WITH TYPE CASTING
# -------------------------------------------------
a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))

print("The sum is:", a + b)


# -------------------------------------------------
# 9. MODULUS OPERATOR (REMAINDER)
# -------------------------------------------------
p = 5
q = 2

print("\nDivision:", p / q)
print("Remainder:", p % q)


# -------------------------------------------------
# 10. GREATER / SMALLER NUMBER
# -------------------------------------------------
a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(a, "is greater than", b)
elif b > a:
    print(b, "is greater than", a)
else:
    print("Both numbers are equal")


# -------------------------------------------------
# 11. AVERAGE OF TWO NUMBERS
# -------------------------------------------------
a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))

average = (a + b) / 2
print("Average:", average)


# -------------------------------------------------
# 12. SQUARE AND CUBE OF A NUMBER
# -------------------------------------------------
number = int(input("\nEnter a number: "))

square = number ** 2
cube = number ** 3

print("Square:", square)
print("Cube:", cube)
