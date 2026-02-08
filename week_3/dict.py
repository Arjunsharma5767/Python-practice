'''
# -------------------------------
# 📌 DICTIONARIES IN PYTHON
# -------------------------------

# A dictionary is a collection of key-value pairs.
# Think of it like a real-world dictionary: a word (key) maps to its meaning (value).

# Example:
marks = {
    "Arjun": 100,
    "Arun": 120,
    "Akshit": 130,
    "Aradhana": 140,
}

# ✅ Accessing values using keys
print(marks["Arjun"])   # Output: 100

# ✅ Checking type
print(type(marks))      # Output: <class 'dict'>

# -------------------------------
# 🔑 Key Features of Dictionaries
# -------------------------------
# 1. Keys must be unique (no duplicates).
# 2. Keys must be immutable types (strings, numbers, tuples).
# 3. Values can be of any type (int, str, list, dict, etc.).
# 4. Dictionaries are unordered (before Python 3.7), but from 3.7+ they preserve insertion order.

# -------------------------------
# 🛠 Common Dictionary Operations
# -------------------------------

# Adding a new key-value pair
marks["Aman"] = 95

# Updating an existing value
marks["Arjun"] = 105

# Deleting a key-value pair
del marks["Arun"]

# Checking if a key exists
print("Akshit" in marks)   # True

# Getting all keys
print(marks.keys())        # dict_keys(['Arjun', 'Akshit', 'Aradhana', 'Aman'])

# Getting all values
print(marks.values())      # dict_values([105, 130, 140, 95])

# Getting all items (key-value pairs)
print(marks.items())       # dict_items([('Arjun', 105), ('Akshit', 130), ...])

# Safe value retrieval (avoids KeyError)
print(marks.get("Arun", "Not Found"))  # Output: Not Found

# Iterating through dictionary
for name, score in marks.items():
    print(name, ":", score)

# -------------------------------
# 📚 Dictionary Methods
# -------------------------------
# clear()   → removes all items
# copy()    → returns a shallow copy
# pop(key)  → removes item with given key
# popitem() → removes last inserted item
# update()  → merges another dictionary

# Example:
extra_marks = {"Ravi": 110, "Sita": 115}
marks.update(extra_marks)
print(marks)

# -------------------------------
# ⚡ Dictionary Comprehension
# -------------------------------
# Quick way to build dictionaries
squares = {x: x**2 for x in range(5)}
print(squares)   # {0:0, 1:1, 2:4, 3:9, 4:16}


# -------------------------------
# 📌 SETS IN PYTHON
# -------------------------------

# A set is a collection of unique, unordered elements.
# Think of it like a bag of distinct items — duplicates are automatically removed.

# Example:
fruits = {"apple", "banana", "cherry", "apple"}  # duplicate 'apple' ignored
print(fruits)   # Output: {'apple', 'banana', 'cherry'}

# ✅ Checking type
print(type(fruits))   # Output: <class 'set'>

# -------------------------------
# 🔑 Key Features of Sets
# -------------------------------
# 1. No duplicate elements.
# 2. Unordered (no indexing).
# 3. Elements must be immutable (numbers, strings, tuples).
# 4. Sets are mutable (we can add/remove elements).

# -------------------------------
# 🛠 Common Set Operations
# -------------------------------

# Adding elements
fruits.add("orange")

# Removing elements
fruits.remove("banana")   # KeyError if not found
fruits.discard("grape")   # No error if not found

# Checking membership
print("apple" in fruits)   # True

# Length of set
print(len(fruits))

# -------------------------------
# ⚡ Set Mathematical Operations
# -------------------------------
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A.union(B))        # {1,2,3,4,5,6}
print(A.intersection(B)) # {3,4}
print(A.difference(B))   # {1,2}
print(B.difference(A))   # {5,6}
print(A.symmetric_difference(B)) # {1,2,5,6}

# -------------------------------
# 📚 Set Methods
# -------------------------------
# add()       → add element
# clear()     → remove all elements
# copy()      → shallow copy
# remove()    → remove element (error if not found)
# discard()   → remove element (no error if not found)
# pop()       → remove random element
# union()     → combine sets
# intersection() → common elements
# difference()   → elements in one but not the other
# symmetric_difference() → elements not common

# -------------------------------
# ⚡ Set Comprehension
# -------------------------------
squares_set = {x**2 for x in range(5)}
print(squares_set)   # {0, 1, 4, 9, 16}
'''


'''
marks = {

"Arjun" : 100,
"Arun" : 120,
"Akshit" : 130,
"Aradhana" : 140,
}

print(marks, type(marks))
print(marks["Arjun"])
'''
'''
# ============================================================
# Dictionary Methods in Python
# ============================================================

a = {
    "key": "value",
    "harry": "code",
    "marks": 100,
    "list": [1, 2, 9]
}

# ------------------------------------------------------------
# 1. get(key, default)
# Returns value of the given key
# If key does not exist, returns None or default value
# ------------------------------------------------------------
print(a.get("marks"))          # 100
print(a.get("cycle"))          # None
print(a.get("cycle", 0))       # 0 (default value)

# ------------------------------------------------------------
# 2. keys()
# Returns all keys of the dictionary
# ------------------------------------------------------------
print(a.keys())                # dict_keys(['key', 'harry', 'marks', 'list'])

# ------------------------------------------------------------
# 3. values()
# Returns all values of the dictionary
# ------------------------------------------------------------
print(a.values())              # dict_values([...])

# ------------------------------------------------------------
# 4. items()
# Returns key-value pairs as tuples
# ------------------------------------------------------------
print(a.items())               # dict_items([('key','value'), ('harry','code'), ...])

# ------------------------------------------------------------
# 5. update()
# Updates dictionary with new key-value pairs
# If key exists → value will be overwritten
# ------------------------------------------------------------
a.update({"key": "value2", "Arjun": 100})
print(a)

# ------------------------------------------------------------
# 6. pop(key)
# Removes the given key and returns its value
# If key not found → error
# ------------------------------------------------------------
print(a.pop("harry"))           # code
print(a)

# ------------------------------------------------------------
# 7. popitem()
# Removes and returns the last inserted key-value pair
# ------------------------------------------------------------
print(a.popitem())
print(a)

# ------------------------------------------------------------
# 8. clear()
# Removes all elements from the dictionary
# ------------------------------------------------------------
# a.clear()
# print(a)                      # {}

# ------------------------------------------------------------
# 9. copy()
# Creates a shallow copy of dictionary
# ------------------------------------------------------------
b = a.copy()
print(b)

# ------------------------------------------------------------
# 10. setdefault(key, default)
# Returns value if key exists
# If key does not exist → inserts key with default value
# ------------------------------------------------------------
print(a.setdefault("city", "Jammu"))
print(a)

# ------------------------------------------------------------
# 11. fromkeys(keys, value)
# Creates a new dictionary from given keys
# ------------------------------------------------------------
keys = ["name", "age", "course"]
new_dict = dict.fromkeys(keys, "Not Assigned")
print(new_dict)

# ------------------------------------------------------------
# 12. len()
# Returns number of key-value pairs
# ------------------------------------------------------------
print(len(a))

# ------------------------------------------------------------
# 13. in keyword
# Used to check if a key exists
# ------------------------------------------------------------
print("marks" in a)             # True
print("salary" in a)            # False
'''

'''
# Problem 1: Dictionary Creation
words = {
    "apple": "A fruit that is red or green.",
    "banana": "A long yellow fruit.",
    "cat": "A small domesticated carnivorous mammal.",
    "dog": "A domesticated carnivorous mammal that typically has a long snout.",
}
word = input("enter a word:").strip().lower()
if word in words:
    print(f"{word}: {words[word]}")
else:
    print("Word not found in dictionary.")
    '''

# Problem 2: Take 8 integers from user and store them in a empty set and then display the unique numbers
s = set()
'''
num =  int(input("enter a number:"))
s.add(num)
num =  int(input("enter a number:"))
s.add(num)
num =  int(input("enter a number:"))
s.add(num)
num =  int(input("enter a number:"))
s.add(num)
num =  int(input("enter a number:"))
s.add(num)
num =  int(input("enter a number:"))
s.add(num)
num =  int(input("enter a number:"))
s.add(num)
num =  int(input("enter a number:"))
s.add(num)
print("Unique numbers are:", s)

# method 2
for i in range (8):
    num = int(input("enter a number:"))
    s.add(num)
print("Unique numbers are:", s)
'''

'''
# Problem 3: can we have a set with 18 (int) and "18" (str) as two values in it?
s = set()
s.add(18)
s.add("18")
print(s)  # Output: {18, '18'} - both values coexist as they are of different types
'''
'''
# Problem 4: what will be the length of the following set?
s =  set()
s.add(20)
s.add(20.0)
s.add("20")
print (s)
print(len(s))

# Output: 2 - 20 and 20.0 are considered the same in a set, while "20" is different 
'''

'''
# Problem 5
s = {}
# what is the type of s?
print(type(s))
'''


# Problem 6: Create an empty dictionary. Allow 4 friends to enter their favorite language as 
# value and use key as their names. Assume that the names are unique.

'''
d = {}

for i in range(4):
    name = input("Enter your name: ").strip()
    language = input("Enter your favorite language: ").strip()
    d[name] = language
    print("Favorite languages:", d)

name = input("Enter your name: ").strip()
language = input("Enter your favorite language: ").strip()
d.update ({name : language})

name = input("Enter your name: ").strip()
language = input("Enter your favorite language: ").strip()
d.update ({ name : language})

name = input("Enter your name: ").strip()
language = input("Enter your favorite language: ").strip()
d.update ({name : language})

name = input("Enter your name: ").strip()
language = input("Enter your favorite language: ").strip()
d.update ({name : language})

print("Favorite languages:", d)
'''


'''
# problem 7: If the names of 2 friends are same; what will happen to the program in problem 6?
d = {}
for i in range(2):
    name = input("Enter your name: ").strip()
    language = input("Enter your favorite language: ").strip()
    d[name] = language
    print("Favorite languages:", d)
# If two friends enter the same name, the latter entry will overwrite the former in the dictionary.
'''

'''
# problem 8: How to delete a key-value pair from a dictionary?
d = {
    "Alice": "Python",
    "Bob": "Java",
    "Charlie": "C++"
}
# Deleting using del
del d["Bob"]
print(d)
# Deleting using pop()
d.pop("Alice")
print(d)
'''
'''
# problem 9: Can you change the values inside a list which is contained in set S?
s = {8, 7, 12, "Harry", [1,2]}  
# No, you cannot have a list inside a set because lists are mutable and sets require their elements to be immutable.
'''