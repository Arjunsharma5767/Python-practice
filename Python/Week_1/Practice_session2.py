
# Day 02: Python Variables, Data Types, and Operators

'''
#  working with
# variables and identifiers in python
# A variable is a named location used to store data in the memory. 
# An identifier is the name used to identify a variable, function, class, module, or other object.
a = 1 
b = 2
c = a + b
name = "Arjun" 
# name is the variable here which stores the string Arjun
Fame = name
# printing the variables Fame is the identifier here which stores the value of variable name
print("Hello", Fame)
# operations performed on variables
print("Sum of", a, "and", b, "is", c)
'''

'''
# data types in python
# Text type: string
name = "Arjun"
print("Name:", name)

# Numeric types: int, float, complex
age = 21  # int
height = 5.6  # float
complex_num = 2 + 3j  # complex
print("Age:", age)
print("Height:", height)
print ("Complex Number:", complex_num)

# Boolean type
is_student = True
print("Is Student:", is_student)

# List type
fruits = ["apple", "banana", "cherry"]
print("Fruits:", fruits)
tuple_fruits = ("apple", "banana", "cherry")
print("Tuple Fruits:", tuple_fruits)

# Dictionary type
dict_example = {"name": "Arjun", "age": 25}
print(dict_example)
'''




'''
# Operators in Python
#Variables
a = 10
b = 3
# Operations
c=a+b
d=a-b
e=a*b
f=a/b
g=a%b
h=a**b
'''



'''
# Arithmetic Operators
print("Addition:", c)
print("Subtraction:", d)   
print("Multiplication:", e)
print("Division:", f)
print("Modulus:", g)
print("Exponentiation:", h)
'''




'''
# Comparison Operators
print("Is a equal to b?", a == b)
print("Is a not equal to b?", a != b)
print("Is a greater than b?", a > b)
print("Is a less than b?", a < b)
print("Is a greater than or equal to b?", a >= b)
print("Is a less than or equal to b?", a <= b) 
'''




'''
# Assignment Operators
a = c
print("Value of c after assignment:", a)
a += 5
print("Value of c after a += 5:", a)
a *= 2
print("Value of c after a *= 2:", a)
a -= 4
print("Value of c after a -= 4:", a)
'''


'''
# Logical Operators
x = True or False
# Truth table for 'or' operator
print ("Result of True or False:", True or False)
print ("Result of True or True:", True or True)
print ("Result of False or True:", False or True)
print ("Result of False or False:", False or False )

# Truth table for 'and' operator
print ("Result of True and False:", True and False)
print ("Result of True and True:", True and True)
print ("Result of False and True:", False and True)
print ("Result of False and False:", False and False)

# Truth table for 'not' operator
print("Result of not True:", not True)
print("Result of not False:", not False)
'''


'''
# Type() function and Type Casting
# Using type() function
var1 = 10
var2 = 5.5
var3 = "Hello"
print("Type of var1:", type(var1))
print("Type of var2:", type(var2))  
print("Type of var3:", type(var3))

# Type Casting
int_var = 10
float_var = float(int_var)  # int to float
str_var = str(int_var)      # int to string
double_var = float_var * 2.0  # float operation
print("Integer to Float:", float_var)
print("Integer to String:", str_var)
print("Type of int_var:", type(int_var))
'''

'''
# Input() function with type casting
a = input("Enter first number: ") #input() function takes input from the user as a string a
b = input("Enter second number: ") #input() function takes input from the user as a string b
# Converting string inputs to integers and calculating sum (Type casting)
sum = int(a) + int(b)
print("The sum of", a, "and", b, "is", sum)



# Input() function without type casting
a = int(input("Enter first number: ")) #input() function takes input from the user as a string a
b = int(input("Enter second number: ")) #input() function takes input from the user as a string b
# Converting string inputs to integers and calculating sum (Type casting)
sum = (a) + (b)
print("The sum of", a, "and", b, "is", sum)
'''

'''
# Finding a remainder using modulus operator
a = 5
b = 2
divide = a / b
print("The division of", a, "by", b, "is", divide)
remainder = a % b
print("The remainder when", a, "is divided by", b, "is", remainder)
'''

'''
# another type function example
a=10
b=3.5
c="Hello"
print("Type of a:", type(a))
print("Type of a:", type(b))
print("Type of a:", type(c))
'''

'''
# greater and smaller code
a= int (input("Enter first number:"))
b= int (input("Enter second number:"))

# print ("Is a greater than b?",a>b)
# print ("Is a smaller than b?",a<b)

if a>b:
    print(a,"is greater than", b)
elif a<b:
    print(b,"is greater than", a)
else:
    print("Both are equal")
    '''


'''
# Average code
a= int (input("Enter first number:"))
b= int (input("Enter second number:"))
c= a+b
average= c/2
# or (a+b)/2
print("The average of", a, "and" , b, "is", average)
'''

'''
# code to calculate the square and cubeof a number entered by the user
a= int (input("Enter first number:"))
b= a*a
c= a*a*a
#  b= a**2
# c= a**3

# or (a+b)/2
print("The square of",a,"is", b)
print("The cube of",a,"is", c)

# (a^2) and (a^3) are not used in python for square and cube
'''
