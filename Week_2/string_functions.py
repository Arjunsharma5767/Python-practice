'''
================================================================================
Block 1: String Manipulation Methods
================================================================================
'''

'''
# upper() → makes every letter BIG
# lower() → makes every letter small
# title() → makes the first letter of each word big
# capitalize() → makes only the first letter of the whole sentence big
# swapcase() → flips big letters to small and small letters to big
# casefold() → turns letters small and changes special characters (like ß) for comparison

text = "hElLo PyThOn wOrLd"

print("upper:", text.upper())        # HELLO PYTHON WORLD
print("lower:", text.lower())        # hello python world
print("title:", text.title())        # Hello Python World
print("capitalize:", text.capitalize())   # Hello python world
print("swapcase:", text.swapcase())  # HeLlO pYtHoN WoRlD

special_text = "Straße"   # German word with ß

print("lower() on 'Straße':", special_text.lower())      # straße
print("casefold() on 'Straße':", special_text.casefold())   # strasse
'''

'''
================================================================================
Block 2: Basic String Slicing
================================================================================
'''

'''
name = "Harry"
nameshort = name[0:3]
print(nameshort)

namemoreshort = name[-4:-1]
print(namemoreshort)
'''

'''
================================================================================
Block 3: Reversing a String using a Loop
================================================================================
'''

'''
name = "Harry"
reversedname = ""

for char in name:
    reversedname = char + reversedname

if len(reversedname) == len(name):
    print(reversedname)
'''

'''
================================================================================
Block 4: Slicing with Step Value
================================================================================
'''

'''
name = "abcdefghijklmnopqrstuvwxyz"

# Prints every second character starting from index 1
print(name[1:27:3])

# Prints the string from the 3rd to last character to the end
# print(name[-27:])
'''

'''
================================================================================
Block 5: String Replace and Endswith Methods
================================================================================
'''

'''
mystring = "Arjun_sharma"
mystring = mystring.replace("_", " ")
print(mystring)

mystringack = mystring.endswith("am")
print(mystringack)
'''

'''
================================================================================
Block 6: Escape Sequence Characters
================================================================================
'''

'''
mystring = "Hello \nWorld"           # Newline
print(mystring)

mystring2 = "Hello \tWorld"          # Tab
print(mystring2)

mystring3 = "Hello \\World"          # Backslash
print(mystring3)

mystring4 = "Hello \'World\'"        # Single Quote
print(mystring4)

mystring5 = "Hello \"World\""        # Double Quote
print(mystring5)

mystring6 = "Hello \rWorld"          # Carriage Return
print(mystring6)

mystring7 = "Hello \bWorld"          # Backspace
print(mystring7)

mystring8 = "Hello \fWorld"          # Form Feed
print(mystring8)

mystring9 = "Hello \vWorld"          # Vertical Tab
print(mystring9)

mystring10 = "Hello \aWorld"         # ASCII Bell
print(mystring10)

mystring11 = "Hello \0World"         # Null character
print(mystring11)

mystring12 = "Hello \N{SNOWMAN}World"  # Unicode Character by Name
print(mystring12)

mystring13 = "Hello \u2602World"    # Unicode Character (Umbrella)
print(mystring13)

mystring14 = "Hello \U0001F600World"  # Unicode Character (Grinning Face)
print(mystring14)

mystring15 = "Hello \x48World"      # Hexadecimal Character
print(mystring15)

mystring16 = "Hello \b\bWorld"      # Double Backspace
print(mystring16)

mystring17 = "Hello \t\tWorld"      # Double Tab
print(mystring17)

mystring18 = "Hello \n\nWorld"      # Double Newline
print(mystring18)

mystring19 = "Hello \r\rWorld"     # Double Carriage Return
print(mystring19)

mystring20 = "Hello \f\fWorld"     # Double Form Feed
print(mystring20)

mystring21 = "Hello \v\vWorld"     # Double Vertical Tab
print(mystring21)

mystring22 = "Hello \a\aWorld"     # Double ASCII Bell
print(mystring22)

mystring23 = "Hello \0\0World"     # Double Null character
print(mystring23)

mystring24 = "Hello \N{SNOWMAN}\N{SNOWMAN}World" # Double Snowman
print(mystring24)

mystring25 = "Hello \u2602\u2602World" # Double Umbrella
print(mystring25)

mystrig26 = "Hello world \"Arjun\"" # Mixed quotes
print(mystrig26)
'''

'''
================================================================================
Block 7: Strip(), Lstrip(), and Rstrip() Functions
================================================================================
'''

'''
myname = "   Arjun \nSharma   "
myname2 = "###Arjun \nSharma###"

print(myname.strip())         # Removes leading/trailing whitespace and newlines
print(myname2.strip("#"))      # Removes specific characters

print(myname.lstrip())         # Removes leading whitespace
print(myname2.lstrip("#"))     # Removes leading specific characters

print(myname.rstrip())         # Removes trailing whitespace
print(myname2.rstrip("#"))     # Removes trailing specific characters
'''

'''
================================================================================
Block 8: Practice Set 1 (Input and f-strings)
================================================================================
'''

'''
name = input("Enter your name: ")
# print("Hello " + name.strip() + " Good Afternoon")
print(f"Good Afternoon, {name}")
'''

'''
================================================================================
Block 9: Practice Set 2 (Datetime and Template Replacement)
================================================================================
'''

'''
import datetime

now = datetime.datetime.now()
name = input("Enter your name: ")

letter = "Dear <|Name|>, \n you are selected! \n Congratulations! \n Have a great day ahead. \n Thanks & Regards, \n <|Date|>"

print(letter.replace("<|Name|>", name).replace("<|Date|>", str(now.date())))
'''

'''
================================================================================
Block 10: Practice Set 3 (Find Method)
================================================================================
'''

'''
name = "Arjun is a Good  boy"
# Finds the index of the first occurrence of double space
print(name.find("  "))
'''

'''
================================================================================
Block 11: Practice Set 4 (Replace and String Immutability)
================================================================================
'''

'''
name = "Arjun is a Good  boy"
name.find("  ")

# This prints the modified string but does not change 'name' itself
print(name.replace("  ", " "))

# Strings are immutable: executing functions on them does not change the original
# variable unless the result is assigned back to the variable.
print(name)
'''

'''
================================================================================
Block 12: Practice Set 5 (Multiline String)
================================================================================
'''

'''
letter = "Dear Arjun, \nNice to meet you. \nI hope you are doing good. \n\tHave a nice day. \nThanks & Regards, \nSharma"
print(letter)
'''