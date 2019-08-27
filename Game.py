board = ['1*', '2*', '3*', '4*', '5*', '6*', '7*', '8*', '9*']
piece = ' '
computer_piece = ' '


def display_board(start_board, loops, rows):
    while loops < rows:
        if loops >= 1:
            loops += 2
        print(' | ' + start_board[loops] + ' | ' + start_board[loops + 1] + ' | ' + start_board[loops + 2] + ' | ')
        print(' --------------')
        loops += 1


def heading():
    print("Tic-Tac-Toe")
    print('By: Howard Thomas')


def menu():
    global piece
    user_input = input("Do you want to play? (yes or no) ")
    if user_input.lower() == 'yes' or 'y':
        print('Lets get started')
        piece = input('What letter would you like to be? (X or O) ').upper()
        setGamePiece(piece)
        display_board(board, 0, 5)
    elif user_input.lower() == 'no' or 'n' or 'exit':
        print('Thanks for playing')
    else:
        print('Input invalid... please try again')
        print('Hint: Use y or yes to play and no or n to exit')
        menu()


def setGamePiece(game_piece):
    global computer_piece
    if game_piece.upper() == 'X':
        computer_piece = 'O'
    elif game_piece.upper() == 'O':
        computer_piece = 'X'


def game(game_piece, comp_piece, game_board):
    counter = 1
    playing = True
    while playing:
        if counter == 1:
            try:
                move = int(input('Where would you like to place you piece? '))
                if 0 < move < 11:
                    game_board[move - 1] = game_piece
                    display_board(board, 0, 5)
                    counter = 2
                else:
                    print('The number input was not a valid number')
            except:
                print('Please Type a Number')
        elif counter == 2:
            print("Computer's Turn...{}".format(comp_piece))
            counter = 1


def winning(game_board):
    pass


menu()
print(piece)
print(computer_piece)
game(piece, computer_piece, board)
