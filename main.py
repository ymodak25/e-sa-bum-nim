import pyttsx3

def ShoutText(text):
    engine = pyttsx3.init()
    engine.say(text)
    print(text)
    engine.runAndWait()
    engine.stop()
    return



""" This gives us what form to look at, for example in this case it is tk1: 
file1 = open('tk1.txt', 'r')
"""

file1 = open('tk1.txt', 'r')
Lines = file1.readlines()

count = 0
# Strips the newline character
for line in Lines:
    count += 1
    ShoutText(line.strip())
    print("Line{}: {}".format(count, line.strip()))
