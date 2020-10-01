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
current_player = 'X'

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
    if winner == 'X' or winner == 'O':
        print(winner + ' won.')
    elif winner == None:
        print('Tie.')

# handle a single turn of arbitrary player
def handle_turn(player):

    print(player + '\'s turn.')
    position = input('choose a position from 1-9: ')

    valid = False
    while not valid:

        while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            position = input('invalid input. Choose 1-9: ')

        # first of all beacuse positon is a string we have to change it into integer
        position = int(position) - 1

        if board[position] == '-':
            valid = True
        else:
            print('you can\'t go there, Go again.')


    board[position] = player
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
        winner = row_winner
    elif colum_winner:
        winner = colum_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return



def check_rows():
    # setup global variables
    global game_still_going
    # check if any of the rows have all the same value (and is not empty)
    row_1 = board[0] == board[1] == board[2] != '-'
    row_2 = board[3] == board[4] == board[5] != '-'
    row_3 = board[6] == board[7] == board[8] != '-'
    # if any row does have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    # return a winner (x or o)
    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]
    return


def check_colums():
    # setup global variables
    global game_still_going
    # check if any of the colums have all the same value (and is not empty)
    column_1 = board[0] == board[3] == board[6] != '-'
    column_2 = board[1] == board[4] == board[7] != '-'
    column_3 = board[2] == board[5] == board[8] != '-'
    # if any column does have a match, flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    # return a winner (x or o)
    if column_1:
        return board[0]
    if column_2:
        return board[1]
    if column_3:
        return board[2]
    return


def check_diagonals():
    # setup global variables
    global game_still_going
    # check if any of the diagonals have all the same value (and is not empty)
    diagonal_1 = board[0] == board[4] == board[8] != '-'
    diagonal_2 = board[2] == board[4] == board[6] != '-'
    # if any diagonal does have a match, flag that there is a win
    if diagonal_1 or diagonal_2:
        game_still_going = False
    # return a winner (x or o)
    if diagonal_1:
        return board[0]
    if diagonal_2:
        return board[2]
    return


def check_if_tie():
    global game_still_going
    if '-' not in board:
        game_still_going = False
    return


def flip_player():
    # global varible we need
    global current_player
    #if the current player was X, then change it to O
    if current_player == 'X':
        current_player = 'O'
    # if the current player was O, then change it to X
    elif current_player == 'O':
        current_player = 'X'
    return


play_game()
