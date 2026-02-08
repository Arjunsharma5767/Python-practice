# =========================================================
# PYTHON SET METHODS AND STRING OPERATIONS
# Method CODE → multiline comments
# Notes → single-line comments
# =========================================================


# -------------------- SET METHODS --------------------

# add() → adds an element to the set
"""
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)
"""


# remove() → removes an element, gives error if not found
"""
my_set = {1, 2, 3}
my_set.remove(2)
print(my_set)
"""


# discard() → removes element, no error if element is missing
"""
my_set = {1, 2, 3}
my_set.discard(10)
print(my_set)
"""


# union() → combines elements of two sets
"""
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print(set_a.union(set_b))
"""


# intersection() → common elements from both sets
"""
set_a = {1, 2, 3}
set_b = {2, 3, 4}
print(set_a.intersection(set_b))
"""


# difference() → elements present only in first set
"""
set_a = {1, 2, 3}
set_b = {2, 3, 4}
print(set_a.difference(set_b))
"""


# -------------------- STRING OPERATIONS --------------------

# upper() → converts string to uppercase
"""
text = "python"
print(text.upper())
"""


# lower() → converts string to lowercase
"""
text = "PYTHON"
print(text.lower())
"""


# strip() → removes extra spaces from start and end
"""
text = "  hello  "
print(text.strip())
"""


# replace() → replaces one word with another
"""
text = "I like Java"
print(text.replace("Java", "Python"))
"""


# split() → converts string into list
"""
text = "Python is easy"
print(text.split())
"""


# join() → joins list elements into a string
"""
words = ["Python", "is", "fun"]
print(" ".join(words))
"""


# find() → finds index of substring
"""
text = "Hello World"
print(text.find("World"))
"""


# count() → counts number of occurrences
"""
text = "banana"
print(text.count("a"))
"""


# string slicing → extracts part of string
"""
text = "Computer"
print(text[0:4])
print(text[::-1])
"""



# 1. Write a program to create a dictionary of Hindi words with values as their English 
# translation. Provide user with an option to look it up!

words = {
    "namaste": "Hello",
    "shukriya": "Thank you",
    "kripya": "Please",
}

# take input and convert it to lowercase
word = input("Enter a Hindi word to translate:\n").lower()
print(words.get(word, "Word not found in dictionary"))
