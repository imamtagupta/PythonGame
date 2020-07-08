########################################################################
#Small mini tic-tac-toe game to run on console using some basic operation.
########################################################################


=============TIC TAC TOE GAME ================

#------------Global Variables---------------------
board = ["-","-","-",
         "-","-","-",
         "-","-","-",]

#If game is still running
game_still_going = True

#Who's turn is it?
current_player = "X"

#Who won? or it's tie?
winner = None


def display_board():
    print(board[0]," | ",board[1]," | ",board[2])
    print(board[3], " | ", board[4], " | ", board[5])
    print(board[6], " | ", board[7], " | ", board[8])

#Start playing tic tac toe
def play_game():

    #displaying the board
    display_board()

    #while game is  still running
    while game_still_going:

        #Handle a single turn of an arbitrary player
        handle_turn(current_player)

        #check is the game is over
        check_if_game_over()

        #flip to other player
        flip_player()

    #if game has ended
    if winner == "X" or winner == "O":
        print(winner," won.")
    elif winner == None:
        print("Tie.")




def handle_turn(player):
    print(player,"'s turn")

    position = input("Enter a position from 1-9: ")

    valid = False
    while not valid:

        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input("Enter a position from 1-9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You cant go there, Go again")

    board[position] = player
    display_board()

def check_if_game_over():
    check_if_win()
    check_if_tie()


def check_if_win():
    #declaing gloval variable
    global winner

    # check rows
    row_winner = check_rows()

    # check columns
    column_winner = check_columns()

    # check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    pass


def check_rows():

    #Setup global variable
    global game_still_going

    #check if any rows have same value (and it is not empty)
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"


    if row1 | row2 | row3:
        game_still_going = False

    #To get the player who is winning.
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return


def check_columns():
    #check if any columns have same value.
    col1 = board[0] == board[3] == board[6] != "-"
    col2 = board[1] == board[4] == board[7] != "-"
    col3 = board[2] == board[5] == board[8] != "-"

    if col1 | col2 | col3:
        game_still_going = False

    # To get the player who is winning.
    if col1:
        return board[0]
    elif col2:
        return board[1]
    elif col3:
        return board[2]
    return


def check_diagonals():

    dig1 = board[0] == board[4] == board[8] != "-"
    dig2 = board[2] == board[4] == board[6] != "-"

    if dig1 | dig2:
        game_still_going = False

    if dig1:
        return board[0]
    elif dig2:
        return  board[2]
    return

def check_if_tie():
    global game_still_going


    if "-" not in board:
        game_still_going = False
    return

def flip_player():
    global current_player

    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return
  
#Start playing the game.
play_game()
