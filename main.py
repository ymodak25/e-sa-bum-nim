import pyttsx3

def ShoutText(text):
    engine = pyttsx3.init()
    engine.say(text)
    print(text)
    engine.runAndWait()
    engine.stop()
    return



# Using read lines()
file1 = open('kmg.txt', 'r')
Lines = file1.readlines()

count = 0
# Strips the newline character
for line in Lines:
    count += 1
    ShoutText(line.strip())
    print("Line{}: {}".format(count, line.strip()))
