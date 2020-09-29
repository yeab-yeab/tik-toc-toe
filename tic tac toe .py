# ----- Global Variables -----

# Game board
board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

# If game is still going
game_still_going = True

# who won? or tie?
winner = None

# whose turn is it
current_player = 'x'

# display board
def display_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])

# Play a game of tic tac toe
def play_game():

    # the first thing you wanna do is display the initial board
    display_board()

    # while the game is still going
    while game_still_going:

        # hundle a single turn of an arbitrary player
        handle_turn(current_player)

        # check if the game has ended
        check_if_game_over()

        # flip to the other player
        flip_player()

    # the game has ended
    if winner == 'x' or winner == 'o':
        print(winner + 'won.')
    elif winner == None:
        print('Tie.')

# handle a single turn of arbitrary player
def handle_turn(player):
    position = input('choose a position from 1-9: ')
    # first of all beacuse positon is a string we have to change it into integer
    position = int(position) - 1

    board[position] = 'x'
    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():

    # setup global variables
    global winner

    # check rows
    row_winner = check_rows()
    # check column
    colum_winner = check_colums()
    # check diagonal
    diagonal_winner = check_diagonals()

    # get the winner
    if row_winner:
        winner = row_winner()
    elif colum_winner:
        winner = colum_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = none
    return



def check_rows():
    return


def check_colums():
    return


def check_diagonals():
    return


def check_if_tie():
    return


def flip_player():
    return


play_game()
