# Jenny You
# Do not grade :)

import random

ALL_COLORS = ['red','orange','yellow','green','blue','purple']

def hiddenColors():
    secret = []
    for i in range(4):
        color = ALL_COLORS[random.randint(0, len(ALL_COLORS)-1)]
        secret.append(color)
    print("The secret code has been chosen. You have 10 tries to guess the code.")
    return secret

def getGuess():
    print("-----------------------------")
    print("Make a guess of four colors:")
    print("0  -  red")
    print("1  -  orange")
    print("2  -  yellow")
    print("3  -  green")
    print("4  -  blue")
    print("5  -  purple")
    print("-----------------------------")

    guess = []
    for i in range(4):
        color = validColor()
        guess.append(ALL_COLORS[color])
    print("-----------------------------")
    print("Your guess is:")
    print(guess)
    return guess

def validColor():
    OK = False
    while OK == False:
        try:
            color = int(input("Guess color:"))
            if color < 0 or color > 5:
                print("Invalid guess, try again:")
            else:
                OK = True
        except ValueError:
            print("Invalid number, try again:")
    return color
        

def checkGuess(guess, secret):
    clue = []
    correct = []
    guess2 = guess.copy()
    secret2 = secret.copy()
    for i in range(len(guess)):
        if guess[i] == secret[i]:
            clue.append(2)
            guess2.remove(guess[i])
            secret2.remove(guess[i])
    for i in range(len(guess2)):
        if guess2[i] in secret2:
            clue = [1] + clue
    print("Your clue is:", clue)
    return clue

def main(seedValue):
    random.seed(seedValue)
    secret = hiddenColors()
    guesses = 10
    found = False

    while guesses > 0:
        guess = getGuess()
        if guess == secret:
            found = True
            guesses -= 1
            print("Correct! You finished in", 10-guesses, "guesses")
            again = input("Would you like to play again? (Y/N)")
            if again == "y":
                secret = hiddenColors()
                guesses = 10
            else:
                print("Thank you for playing. Good-bye!")
                guesses = 0
        else:
            clue = checkGuess(guess,secret)
            guesses -= 1
            if guesses == 0 and found == False:
                print("No more guesses, the hidden colors were:")
                print(secret)
                again = input("Would you like to play again? (Y/N)")
                if again == "y":
                    secret = hiddenColors()
                    guesses = 10
                else:
                    print("Thank you for playing. Good-bye!")
                    guesses = 0
            else:
                print("You have ", guesses, "guesses left")
    
    
