"""
==================================================
PYTHON PRACTICE EXERCISES
Topics: Basics, REPL, Modules, Text-to-Speech, OS
==================================================
"""

# -------------------------------------------------
# Exercise 1: Print Poem
# -------------------------------------------------
print("Twinkle, twinkle, little star,")


# -------------------------------------------------
# Exercise 2: Read–Evaluate–Print Loop (REPL Example)
# -------------------------------------------------
for i in range(2, 21):
    print("5 x", i, "=", 5 * i)


# -------------------------------------------------
# Exercise 3: Jokes Program
# -------------------------------------------------
import pyjokes

def random_joke():
    """Prints a random joke using pyjokes library"""
    print("Getting a random joke for you:")
    joke = pyjokes.get_joke()
    print(joke)

if __name__ == "__main__":
    random_joke()


# -------------------------------------------------
# Exercise 4: Text to Speech
# -------------------------------------------------
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Set voice (change index if required)
engine.setProperty('voice', voices[1].id)

# Slow down speech rate
engine.setProperty('rate', 130)

engine.say("Hello! This is a text to speech example.")
print("How I wonder what you are!")
print("Up above the world so high,")

engine.runAndWait()


# -------------------------------------------------
# Exercise 5: List Directory Contents
# -------------------------------------------------
import os

# Select the directory path to list
directory_path = "/"

# Get directory contents
contents = os.listdir(directory_path)

# Print directory contents
for item in contents:
    print(item)
