#-----------------------------------------------------------
# Passwordy
#
# this program selects a random word from a pre-defined
#  list and the user must try to guess the word.
#
#-----------------------------------------------------------

import random

# read the list of keywords and assign to variable
with open('word_dict5.txt') as f:
    poss_keywords = []
    for i in f:
        poss_keywords.append(i.strip())

# function that displays the main menu and stores the user's selection.
def main_menu():
    user_selection = input("""Main Menu
    (p) Play a round
    (i) View instructions
    (q) Quit
    Please select an option: """)
    
    if user_selection.casefold() == 'p':
        round_start()
    elif user_selection.casefold() == 'i':
        rules_game()
    elif user_selection.casefold() == 'q':
        quit_game()
    else:
        input('Invalid selection. Press enter to return to the Main Menu.')
        main_menu()

# function that picks a random word and starts a new round.
def round_start():
    # generate new word
    curr_keyword = choose_pass()
    #print(curr_keyword)
    
    # start regular round loop
    round_loop(curr_keyword)  
    
# function that displays the rules of the game and then returns to the main menu.
def rules_game():
    print("""
    - A random, English keyword will be generated by the computer.
    - Your task is to guess the keyword using clues based on your previous guesses.
    - When you submit a valid guess, the computer will tell you whether each letter is one of three states:
    - You only get 5 guesses, so choose wisely!
    
    \tO --> Correct letter and position
    \tx --> Correct letter but wrong position
    \t- --> Letter is not in the keyword
    
    - Letters can repeat in the word, but it is up to you to figure out if that is the case.
    """)
    input('Press Enter to return to the Main Menu.')
    main_menu()

# function that asks the user to confirm if they want to quit the program.
def quit_game():
    user_selection = input("Quit the program? (y/n): ")
    if user_selection.casefold() == 'y':
        quit()
    else:
        main_menu()

# function that randomly chooses one of the words from the list.
def choose_pass():
    random.seed()
    rand_num = random.randint(0,len(poss_keywords)-1)
    return poss_keywords[rand_num]

# function to inform the user they won.
def winner(r, m, p):
    for i in m:
        print(i)
    print("Password guessed correctly! Congratulations!")
    print("You guessed correctly on round ", r)
    c = input('Would you like to return to the main menu? (y/n)')
    if c.casefold() == 'y' or c.casefold() == 'yes':
        main_menu()
    else:
        quit()

# function to check if a guess is a valid entry.
def valid_guess(guess):
    if len(guess) == 5:
        if guess.casefold() in poss_keywords:
            return 'v' # valid
        else:
            input('Not a valid word. Press Enter to try a new word')
            return 'i' # invalid
    else:
        input('Guesses must be exactly five letters. Press Enter to try a new word')
        return 'l' # too many letters

# function to check guess to password and update board (matrix)
def guess_check(guess, password):
    #print(guess, '\n', password)
    matrix = ''
    for n,v in enumerate(guess):
        if guess[n] == password[n]:
            matrix = matrix + 'O'
        elif password.find(guess[n]) != -1:
            matrix = matrix + 'x'
        else:
            matrix = matrix + '-'
    return matrix
    
# fuction to loop the guesses in a round.
def round_loop(p):

    rnd_cntr = 1
    matrix = []
    
    while rnd_cntr < 6:

        print(f'\nRound: {rnd_cntr}')
        for i in matrix:
            print(i)
        g = input('Enter your five-letter guess: ')
        if valid_guess(g) == 'v':
            matrix.append(guess_check(g, p))
            matrix.append(g.upper())
            if matrix[-2] == 'OOOOO':
                winner(rnd_cntr, matrix, p)
            rnd_cntr += 1
        else:
            continue
    else:
        a = input("""You have run out of guesses. Better luck next time!
Return to the main menu?: """)
        if a.casefold() == 'y' or a.casefold() == 'yes':
            print('menu')
            main_menu()
        else:
            print("quit")
            quit()
            

#---------------------------------------------------------

# Welcome message
print("Welcome to Passwordy! The game of guessing passwords!")

# Start main loop
main_menu()

# for debugging
#print(user_selection)
