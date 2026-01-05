
'''
# Exercise 1:
print ("Twinkle, twinkle, little star,")
'''



'''
# Exercise 2: Read Evaluate Print Loop (REPL) 
for i in range(2,21):
...     print ("5 x", i, "=", 5*i)
...

'''

'''# Exercise 3: Jokes Program
import pyjokes
def random_joke():
    print("Getting a random joke for you:")
    Rucheeta = pyjokes.get_joke()
    print(Rucheeta)
    # So thanks
    # This was My Jokes program and 
    # here i used the Multiline comment
    # This will print a random joke from the pyjokes library and this the statement is a single line comment
if __name__ == "__main__":
    random_joke()
'''

'''
# Exercise 4: Text to Speech
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# Try Indian voice (change index if needed)
engine.setProperty('voice', voices[1].id)
# Slow down the voice
engine.setProperty('rate', 130)
engine.say("Hey baby, you look like a bot.")
print("How I wonder what you are!")
print("Up above the world so high,")
engine.runAndWait()
'''

'''
# Exercise 5: List Directory Contents
import os
# select the directory path you want to list
directory_path = "/"
# list all the contents of the directory
contents = os.listdir(directory_path)
# Finally print the contents of the directory
for item in contents:
    print (item)

'''
