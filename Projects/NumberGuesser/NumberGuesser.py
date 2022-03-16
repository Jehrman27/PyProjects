# NumberGuesser
# this program will randomly generate a number for the user to guess.


import random

userName = "John Doe"
randNum = 0
userGuess = None
guesses = 0


# prompt user for their name and then welcome them
userName = input("Please enter your name:")
print("Welcome to the random number guesser,", userName)

# explain the purpose of the program to the user
print("This program will generate a number from 1 to 10 and then you will try to guess the number.")

# generate the random number and let the user know it is ready
randNum = int(random.randint(1,10))

print("The random number has been generated.")

while True:

    try:
        # prompt the user to enter their guess in range
        userGuess = int(input("Please enter your guess (1-10):"))
    except:
        print("Invalid entry.")
        continue
    
    # print both numbers for testing purposes
    #print("random:", randNum)
    #print("guess:", userGuess)

    # increment guesses
    guesses = guesses + 1
    # test if guess is correct, too high, or too low
    if userGuess == randNum: 
        print("Correct! Congratulations!")
        print("It took you", guesses, "guesses. Nice work.")
        break
    elif userGuess < randNum:
        print("Sorry! Too low.") 
    else:
        print("Sorry! Too high.") # guess isn't equal to or lower than the random number, so must be too high


print("Thanks for playing!")