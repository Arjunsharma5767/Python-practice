# ============================================================================
# PYTHON LISTS 
# ============================================================================
# A list in Python is a built-in data structure used to store multiple values
# in a single variable.
#
# Lists are one of the most commonly used data types in Python.
#
# Key characteristics of Python lists:
# 1. Lists are ORDERED – elements have a defined order and that order does not change.
# 2. Lists are MUTABLE – elements can be changed after the list is created.
# 3. Lists allow DUPLICATE values.
# 4. Lists can store DIFFERENT data types in the same list.
# 5. Lists can contain OTHER LISTS (nested lists).
# 6. Lists are created using square brackets [].
#
# Lists are widely used for:
# - Storing collections of data
# - Iterating over multiple values
# - Implementing stacks, queues, and dynamic arrays
# - Data processing and manipulation
#
# ============================================================================

mylist = ["Arjun", 21 , 12.5 , True , "sharma"]
'''
# List with index example
print(mylist[2])
'''
'''
# List with replace example
mylist[1] = 22  #Unlike strings, lists are mutable
print(mylist[1])
'''
'''
# index calling is same as string index calling
print(mylist[1:4])
'''

'''
# List methods example
mylist.append("New Element")  # Adding an element to the end of the list
print(mylist)
mylist.remove(12.5)  # Removing an element from the list
print(mylist)
l1 = [2,5,8,9,1,3,4,7,6,0]
l1.sort()
print(l1)
l1.reverse()
print(l1)
l1.insert(2,3.3)  # inserting 3.3 at index 2
print(l1)
l1.pop()  # removes the last element
print(l1)
l1.pop(2)  # removes element at index 3
print(l1)
l1.remove(1)
print(l1)
l1.clear()  # removes all elements from the list
print(l1)
'''
'''
=============================================================================
Tuples
=============================================================================
'''

'''
# =============================================================================
# Python Tuples – Methods and Operations
# =============================================================================

# Creating a tuple
a = (1, 45, 55, 55, "Arjun", 12.5, True, False)

# =============================================================================
# 1. count() method
# =============================================================================
# Returns the number of times a specified value appears in the tuple
count_55 = a.count(55)
print(count_55)

# =============================================================================
# 2. index() method
# =============================================================================
# Returns the index of the first occurrence of the specified value
# If the value is not found, it raises a ValueError
index_55 = a.index(55)
print(index_55)

# =============================================================================
# Tuple does NOT support methods like append(), remove(), pop()
# because tuples are immutable (cannot be changed after creation)
# =============================================================================

# =============================================================================
# Tuple Length
# =============================================================================
# len() returns the total number of elements in the tuple
length = len(a)
print(length)

# =============================================================================
# Accessing Elements
# =============================================================================
# Access element using positive index
print(a[1])

# Access element using negative index
print(a[-1])

# =============================================================================
# Tuple Slicing
# =============================================================================
# Slicing returns a new tuple
print(a[0:4])      # From index 0 to 3
print(a[2:])       # From index 2 to end
print(a[:5])       # From start to index 4
print(a[::2])      # Step slicing

# =============================================================================
# Checking Membership
# =============================================================================
# in operator checks whether a value exists in the tuple
print(55 in a)
print("Arjun" in a)
print(100 in a)

# =============================================================================
# Tuple Concatenation
# =============================================================================
# You can join two tuples using + operator
t1 = (1, 2, 3)
t2 = (4, 5)
t3 = t1 + t2
print(t3)

# =============================================================================
# Tuple Repetition
# =============================================================================
# You can repeat tuple elements using * operator
t4 = t1 * 3
print(t4)

# =============================================================================
# Nested Tuples
# =============================================================================
nested_tuple = (1, 2, (3, 4, 5))
print(nested_tuple[2])
print(nested_tuple[2][1])

# =============================================================================
# Tuple Unpacking
# =============================================================================
# Assigning tuple values to variables
x, y, z = (10, 20, 30)
print(x)
print(y)
print(z)

# =============================================================================
# Single Element Tuple
# =============================================================================
# A single element tuple must have a comma
single = (10,)
print(type(single))

# =============================================================================
# Tuple Conversion
# =============================================================================
# Converting list to tuple
list_data = [1, 2, 3]
tuple_data = tuple(list_data)
print(tuple_data)

# Converting tuple to list (useful when modification is needed)
list_again = list(a)
print(list_again)

# =============================================================================
# Looping through a tuple
# =============================================================================
for item in a:
    print(item)

# =============================================================================
# Tuple with different data types
# =============================================================================
mixed = (1, "Python", 3.14, True)
print(mixed) 

'''
'''
# Create a list of marks by taking input from the user
# Problem one 
marks = []
f1 = input("Enter your marks here \t")
marks.append(f1)
f2 = input("Enter your marks here \t")
marks.append(f2)
f3 = input("Enter your marks here \t ")
marks.append(f3)
f4 = input("Enter your marks here \t")
marks.append(f4)
f5 = input("Enter your marks here \t")
marks.append(f5)
f6 = input("Enter your marks here \t")
marks.append(f6)
f7 = input("Enter your marks here \t")
marks.append(f7)
print(marks)
'''
'''
# Problem 2 
# Write a program to accept marks of 6 students and display them in the sorted manner
marks = []
f1 = input("Enter your marks here \t")
marks.append(f1)
f2 = input("Enter your marks here \t")
marks.append(f2)
f3 = input("Enter your marks here \t")
marks.append(f3)
f4 = input("Enter your marks here \t")
marks.append(f4)
f5 = input("Enter your marks here \t")
marks.append(f5)
f6 = input("Enter your marks here \t")
marks.append(f6)

print(marks)
'''
''''
# Problem 3
# Check that tuple type can not be changed in python

a = (34, 2.3, "Arjun")

a[2] = "Sharma"
'''

'''
# Problem 4
# We have a list in which we have to add four numbers and print their sum
l1 = [2,3,4,1]
print(sum(l1)) 
'''
''''
# Problem 4
a = (7,0,8,0,6,4,2,0)
n =  a.count(0)
print(n)
''' 