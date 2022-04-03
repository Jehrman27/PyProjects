"""
Two players can play a game of Tic Tac Toe on the same computer.
"""
import os
import sys
from itertools import cycle


def display_board(box):
    """Prints each arg on its own line.

    box -- state of board as a list to print to the terminal.
    """
    row1 = f'\n  {box[6]} | {box[7]} | {box[8]} \n'
    row2 = f' {box[3]} | {box[4]} | {box[5]} \n'
    row3 = f' {box[0]} | {box[1]} | {box[2]} \n'
    row4 = '-----------\n'
    print(row1, row4, row2, row4, row3)


def clear_screen():
    """Identifies the running OS and clears the terminal."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def validate(box):
    """Returns a list of valid cell indicies.

    box -- current state of game board as a list.
    """
    valid = []
    for index,cell in enumerate(box):
        if cell == ' ':
            valid.append(index+1)

    return valid


def start_game():
    """Initiates the start of a new game."""
    box = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    clear_screen()


    ans = player_input('Are you ready to begin? (y/n): ', False, 'y', 'n')
    if ans == 'y':
        # start game
        pass
    else:
        sys.exit()
    clear_screen()

    p_dict = {'1':'', '2':''}
    p_dict['1'] = player_input(
            'Choose player one\'s token: (X/O): ', True, 'X', 'O'
            )
    if p_dict['1'] == 'O':
        p_dict['2'] = 'X'
    else:
        p_dict['2'] = 'O'
    clear_screen()

    game_end = False
    turn_iter = cycle(['1','2'])
    display_board(box)
    while not game_end:
        valid_cells = validate(box)
        active_player = next(turn_iter)
        move = player_input(
                f'Player {active_player} ({p_dict[active_player]}) '\
                'choose your move: ',
                True,
                *valid_cells
                )
        box = update_board(p_dict[active_player], int(move), box)
        clear_screen()
        display_board(box)
        yyy = check_game_end(box, p_dict[active_player])
        print (yyy)
        if yyy == 'win':
            print(f'Congratulations! Player {active_player} wins!')
            play_again()
        elif yyy == 'tie':
            print('Tie game! No winner this time.')
            play_again()


def player_input(prompt, case_sens, *args):
    """Returns validated user input.

    prompt -- what to ask user when pulling response.
    case_sens -- if validation should consider casing.
    *args -- valid user responses to check for.
    """
    ans = ''
    valid_inputs = [str(item) for item in args]
    if case_sens:
        while str(ans) not in valid_inputs:
            ans = input(prompt)
            if ans not in valid_inputs:
                print('Not a valid response.')
    else:
        while ans.casefold() not in valid_inputs:
            ans = input(prompt)
            ans = ans.casefold()
            if ans not in valid_inputs:
                print('Not a valid response.')
    return ans


def update_board(token, move, box):
    """Returns a list with token added to position move.

    token -- active player's token.
    move -- player's target cell.
    box -- current state of board in a list.
    """
    cell = move-1
    box[cell] = token
    return box


def check_game_end(box, token):
    """Returns if the current state has a win or tie.

    box -- current state of board.
    token -- the token of the last player to make a move.
    """
    rows = [[0,1,2],[3,4,5],[6,7,8]]
    cols = [[6,3,0],[7,4,1],[8,5,2]]
    diags = [[6,4,2],[0,4,8]]
    checks = rows + cols + diags

    for row in checks:
        match = 0
        for cell in row:
            if box[cell] == token:
                match += 1
                if match == 3:
                    return 'win'
            else:
                break
        match = 0
    for cell in box:
        if cell != ' ':
            match += 1
            if match == 9:
                return 'tie'

    return 'continue'


def play_again():
    """Returns if user wants to play again."""
    ans = player_input(
            'Would you like to play again? (y/n): ',
            False,
            'y', 'n'
            )
    if ans == 'y':
        clear_screen()
        start_game()
    else:
        clear_screen()
        sys.exit()


# Starts a fresh game when program is booted.
# Begins all game logic.
start_game()
