"""
--------------------------------------------------
STRINGS IN PYTHON
Topics: String definition, indexing, slicing, reverse indexing
--------------------------------------------------
"""

# Strings in Python can be defined using:
# 1. Single quotes
# 2. Double quotes
# 3. Triple quotes (for multi-line strings)

single_quote_str = 'Hello, World!'
double_quote_str = "Hello, Python!"
triple_quote_str = """This is a multi-line
string in Python."""

print(single_quote_str)
print(double_quote_str)
print(triple_quote_str)


# --------------------------------------------------
# STRING SLICING
# --------------------------------------------------
text = "Sample&StringAS"

short_text = text[0:14]
print("\nOriginal String:", text)
print("Sliced String:", short_text)


# --------------------------------------------------
# STRING INDEXING (FORWARD)
# --------------------------------------------------
print("\nForward Indexing:")

for i in range(len(text)):
    print(f"Character at index {i}: {text[i]}")


# --------------------------------------------------
# STRING INDEXING (REVERSE)
# --------------------------------------------------
print("\nReverse Indexing:")

for i in range(1, len(text) + 1):
    print(f"Character at index -{i}: {text[-i]}")
