import random

# Magic Ball
# the program will allow the user to ask a question and then the program
# will respond with a random answer from a pre-generated list.


# declarations
userQuestion = "Yes?"
randAnswer = "Yes."
answerList = ""

# open file with list of answers
f = open("EightBData.txt", "r")
answerList = f.readlines()

# welcome and propt user - input() allows the user time to read
input("Welcome to the Magic 8 Ball program. This is not a game. Press Enter if you dare...")
userQuestion = input(
    "What yes or no question would you like to ask the wisest "
    "sphere known to mankind?"
                     )

# generate random answer from the list
randAnswer = random.choice(answerList)

# inform and answer the user
input("Contacting the shiny sphere of wisdom...") 
print("It has this to say on the matter:", randAnswer)