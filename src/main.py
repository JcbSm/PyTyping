import datetime
import msvcrt
import random
import os

# Import words
from words import words

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def getPlay():
    return True if input("Want to test your typing speed? (Y/N) ").upper() == 'Y' else False

def printWords(i = 0):
    return print(' '.join(words[i : i+20]))

def printTimer():
    time = round((endTime - datetime.datetime.now()).total_seconds())
    return print("01:00\n" if time > 59 else "00:" + str(time) + "\n")

def test():

    global words, endTime

    random.shuffle(words)

    start = False
    while not start:
        cls() # Clear the terminal
        print("01:00\n")
        printWords() # Print the words, as seen
        start = True if input("Type 'Start' to begin: ").lower() == "start" else False # Check if the user wishes to start.

    # Starting

    currentGuess = "" # Initialise variable.
    cc = 0; ii = 0 # cc - Correct, ii - Incorrect

    endTime = datetime.datetime.now() + datetime.timedelta(minutes = 1)

    while datetime.datetime.now() < endTime:

        cls() # Clear terminal
        printTimer() #
        printWords(cc+ii) # Print words
        print(currentGuess) # Print the current guess as it is

        char = msvcrt.getch() # Await keyboard press

        if char == b'\x08': # if backspace
            currentGuess = currentGuess[:-1] # Remove last char from str

        elif char == b' ': # If space, assume word is finished
            if currentGuess == words[cc+ii]: # If word is typed correctly
                cc += 1 # Increment correct word count
            else:
                ii += 1 # Incremement incorrect word count

            currentGuess = "" # Reset guess string

        else:
            currentGuess = currentGuess + char.decode('utf-8') # Append char to current guess

    return cc, ii

play = getPlay()
while play:

    correct, incorrect = test()
    total = correct + incorrect

    cls()
    # Print stats afterwards
    print("WPM:      " + str(total))
    print("Accuracy: " + str(round(100*correct/(1 if total == 0 else total), 2)) + '%')
    print(" ")

    play = getPlay()