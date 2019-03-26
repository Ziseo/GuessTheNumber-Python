#Guess the number
#Coded by: James Byatte
#Last updated: 08/02/2019
#version: 1.1 Dev

import random

givenRange = int(10)
maxAttempts = int(5)
randomAnswer = int(0)
nGuesses = int(0)
guessRight = False
runGame = True

def startUp():
    print("Coded by: James Byatte")
    print("Last updated: 03/25/2019")
    print("Version: 1.2")
    print()
    print("Welcome to Guess The Number!")
    print("A random number between 0 and your chosen number will be generated. Try to guess the number.")
    print()
   
def RNG (randomAnswer,givenRange):
    randomAnswer = random.randrange(0,givenRange)
    return randomAnswer

def answerCheck(randomAnswer,uAnswer,nGuesses,givenRange) :
    if (uAnswer < 0) or (uAnswer > givenRange - 1):
        print ('The number you entered is not in between', 0, 'and', givenRange - 1)
        return False
    if uAnswer > randomAnswer:
        print("Your guess was high.")
        return False
    if uAnswer < randomAnswer:
        print("Your guess was low.")
        return False
    else:
        print("Correct! You guessed correctly in " + str(nGuesses) + " tries.")
        print()
        return True


def getInput(givenRange,maxAttempts):
    while True:
        givenRange = input("How large of a range? ")
        try:
            givenRange = int(givenRange) + 1
        except:
            print("Not a number. Enter a number.")
            print()
            continue
        break
    while True:
        maxAttempts = input("How many tries do you want? ")
        try:
            maxAttempts = int(maxAttempts)
        except:
            print("Not a number. Enter a number.")
            print()
            continue
        print("Your random number has been generated. Good luck!")
        print()
        break
    return givenRange, maxAttempts

###############################################################################################

startUp()

while runGame == True:
    givenRange, maxAttempts = getInput(givenRange,maxAttempts)
    randomAnswer = RNG(randomAnswer,givenRange)
        
    while guessRight == False:
            if nGuesses >= maxAttempts:
                print("You have failed to guess the number " + str(randomAnswer) + " in " + str(maxAttempts) + " attempts. You lose.")
                print()
                break
            nTriesLeft = maxAttempts - nGuesses
            if nTriesLeft == 1:
                uAnswer = input("You have " + str(nTriesLeft) + " guess left: ")
            else:
                uAnswer = input("You have " + str(nTriesLeft) + " guesses left: ")
            try:
                uAnswer = int(uAnswer)
            except:
                print ("Not a number. Enter a number")
                continue
            nGuesses += 1
            guessRight = answerCheck(randomAnswer,uAnswer,nGuesses,givenRange)
    
    while True:
        playAgain = input("Play again?(y/n) ")
        if playAgain == "y":
           runGame = True
           guessRight = False
           print()
           break
        if playAgain == "n":
            print("You have selected n.")
            runGame = False
            break
        else:
            print("That was neither y or n.")
            continue

print("Good Bye")
