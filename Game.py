import random
# * Variables 
board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
player_piece = ' '
computer_piece = ' '
playing = True

# * display_board method which uses the board, amount of loops and rows to create a tic tac toe board
def display_board(start_board, loops, rows):
    while loops < rows:
        if loops >= 1:
            loops += 2
        print(' | ' + start_board[loops] + ' | ' +
              start_board[loops + 1] + ' | ' + start_board[loops + 2] + ' | ')
        print(' -------------')
        loops += 1

#* Simple heading to start the game
def heading():
    print("Tic-Tac-Toe")
    print('By: Howard Thomas')

# * menu method to allow user to play and exit game as well as choose the piece they want to play with
def menu():
    global player_piece
    user_input = input("Do you want to play? (yes or no) ")
    if user_input.lower() == 'yes' or 'y':
        print('Lets get started')
        player_piece = input(
            'What letter would you like to be? (X or O) ').upper()
        set_game_piece(player_piece)
    elif user_input.lower() == 'no' or 'n' or 'exit':
        print('Thanks for playing')
    else:
        print('Input invalid... please try again')
        print('Hint: Use y or yes to play and no or n to exit')
        menu()

# * Sets game piece for the user and computer player
def set_game_piece(game_piece):
    global computer_piece
    if game_piece.upper() == 'X':
        computer_piece = 'O'
    elif game_piece.upper() == 'O':
        computer_piece = 'X'

# * game method/loop to play through the game
def game():
    global playing
    counter = random.randint(1, 2)
    while playing:
        if counter == 1:
            user_move(player_piece, board)
            if winning_check(board, player_piece):
                print('You have won')
                playing = False
                display_board(board, 0, 5)
            else:
                if not board_check(board):
                    display_board(board, 0, 5)
                    print('Game is a tie')
                    playing = False
                else:
                    counter = 2
        elif counter == 2:
            computer_move(computer_piece, board, player_piece)
            if winning_check(board, computer_piece):
                print('The Computer has won')
                display_board(board, 0, 5)
                playing = False
            else:
                if not board_check(board):
                    display_board(board, 0, 5)
                    print('Game is a tie')
                    playing = False
                else:
                    counter = 1

# * Allows user to move piece to valid spot on the board
def user_move(game_piece, game_board):
    try:
        move = int(input('Where would you like to place you piece? '))
        if 0 < move < 11:
            if moveCheck(game_board, move):
                doMove(game_board, game_piece, move)
            winningCheck(board, game_piece)
        else:
            print('The number input was not a valid number')
    except:
        print('Please Type a Number')
        user_move(player_piece, board)

# * Is the computers move 
def computer_move(comp_piece, game_board, user_piece):
    computer_AI(game_board, comp_piece, user_piece)
    display_board(board, 0, 5)
    winning_check(board, comp_piece)

# * checks if move is valid
def move_check(game_board, move_number):
    if game_board[move_number - 1] != player_piece and game_board[move_number - 1] != computer_piece:
        return True
    else:
        return False

# * does the move if it is valid 
def do_move(game_board, current_piece, move_number):
    game_board[move_number - 1] = current_piece

# * allows computer to see possible moves
def random_move(board, movesList):
    possibleMoves = []
    for i in movesList:
        if move_check(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

# *Check to see if their is any possible moves left to make. if none game is a tie 
def board_check(game_board):
    for i in range(0, 10):
        if move_check(board, i):
            return True
    return False

# * Check to see if anyone wins
def winning_check(game_board, current_player):
    return ((game_board[0] == current_player and game_board[1] == current_player and game_board[2] == current_player) or
            (game_board[3] == current_player and game_board[4] == current_player and game_board[5] == current_player) or
            (game_board[6] == current_player and game_board[7] == current_player and game_board[8] == current_player) or
            (game_board[0] == current_player and game_board[3] == current_player and game_board[6] == current_player) or
            (game_board[1] == current_player and game_board[4] == current_player and game_board[7] == current_player) or
            (game_board[2] == current_player and game_board[5] == current_player and game_board[8] == current_player) or
            (game_board[0] == current_player and game_board[4] == current_player and game_board[8] == current_player) or
            (game_board[2] == current_player and game_board[4] == current_player and game_board[6] == current_player))

# * Computer AI 
def computer_AI(game_board, comp_piece, user_piece):
    move = computer_win(game_board, comp_piece)
    if move != None:
        do_move(game_board, comp_piece, move)
    else:
        move = computer_player_win_check(game_board, user_piece)
        if move != None:
            do_move(game_board, comp_piece, move)
        else:
            move = random_move(game_board, [5])
            if move != None:
                do_move(game_board, comp_piece, move)
            else:
                move = random_move(game_board, [1, 3, 7, 9])
                if move != None:
                    do_move(game_board, comp_piece, move)
                else:
                    move = random_move(game_board, [2, 4, 6, 8])
                    if move != None:
                        do_move(game_board, comp_piece, move)

# * Checks to see if player will win 
def computer_player_win_check(game_board, user_piece):
    for i in range(1, 10):
        copy = board_copy(game_board)
        if move_check(copy, i):
            do_move(copy, user_piece, i)
            if winning_check(copy, user_piece):
                return i


def computer_win(game_board, comp_piece):
    for i in range(1, 10):
        copy = board_copy(game_board)
        if move_check(copy, i):
            do_move(copy, comp_piece, i)
            if winning_check(copy, comp_piece):
                return i

# * Copy's board 
def board_copy(game_board):
    copy_board = []
    for i in game_board:
        copy_board.append(i)
    return copy_board


if __name__ == "__main__":
    heading()
    menu()
    game()
