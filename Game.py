import random

board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
player_piece = ' '
computer_piece = ' '
playing = True


def display_board(start_board, loops, rows):
    while loops < rows:
        if loops >= 1:
            loops += 2
        print(' | ' + start_board[loops] + ' | ' +
              start_board[loops + 1] + ' | ' + start_board[loops + 2] + ' | ')
        print(' -------------')
        loops += 1


def heading():
    print("Tic-Tac-Toe")
    print('By: Howard Thomas')


def menu():
    global player_piece
    user_input = input("Do you want to play? (yes or no) ")
    if user_input.lower() == 'yes' or 'y':
        print('Lets get started')
        player_piece = input(
            'What letter would you like to be? (X or O) ').upper()
        setGamePiece(player_piece)
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


def game():
    global playing
    counter = random.randint(1, 2)
    while playing:
        if counter == 1:
            userMove(player_piece, board)
            if winningCheck(board, player_piece):
                print('You have won')
                playing = False
                display_board(board, 0, 5)
            else:
                if not boardCheck(board):
                    print('Game is a tie')
                    display_board(board, 0, 5)
                    playing = False
                else:
                    counter = 2
        elif counter == 2:
            computerMove(computer_piece, board, player_piece)
            if winningCheck(board, computer_piece):
                print('The Computer has won')
                display_board(board, 0, 5)
                playing = False
            else:
                if not boardCheck(board):
                    print('Game is a tie')
                    display_board(board, 0, 5)
                    playing = False
                else:
                    counter = 1


def userMove(game_piece, game_board):
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
        userMove(player_piece, board)


def computerMove(comp_piece, game_board, user_piece):
    computer_AI(game_board, comp_piece, user_piece)
    display_board(board, 0, 5)
    winningCheck(board, comp_piece)


def moveCheck(game_board, move_number):
    if game_board[move_number - 1] != player_piece and game_board[move_number - 1] != computer_piece:
        return True
    else:
        return False


def doMove(game_board, current_piece, move_number):
    game_board[move_number - 1] = current_piece


def randomMove(board, movesList):
    possibleMoves = []
    for i in movesList:
        if moveCheck(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None


def boardCheck(game_board):
    for i in range(0, 10):
        if moveCheck(board, i):
            return True
    return False


def winningCheck(game_board, current_player):
    return ((game_board[0] == current_player and game_board[1] == current_player and game_board[2] == current_player) or
            (game_board[3] == current_player and game_board[4] == current_player and game_board[5] == current_player) or
            (game_board[6] == current_player and game_board[7] == current_player and game_board[8] == current_player) or
            (game_board[0] == current_player and game_board[3] == current_player and game_board[6] == current_player) or
            (game_board[1] == current_player and game_board[4] == current_player and game_board[7] == current_player) or
            (game_board[2] == current_player and game_board[5] == current_player and game_board[8] == current_player) or
            (game_board[0] == current_player and game_board[4] == current_player and game_board[8] == current_player) or
            (game_board[2] == current_player and game_board[4] == current_player and game_board[6] == current_player))


def computer_AI(game_board, comp_piece, user_piece):
    move = computer_win(game_board, comp_piece)
    if move != None:
        doMove(game_board, comp_piece, move)
    else:
        move = computer_playerWinCheck(game_board, user_piece)
        if move != None:
            doMove(game_board, comp_piece, move)
        else:
            move = randomMove(game_board, [5])
            if move != None:
                doMove(game_board, comp_piece, move)
            else:
                move = randomMove(game_board, [1, 3, 7, 9])
                if move != None:
                    doMove(game_board, comp_piece, move)
                else:
                    move = randomMove(game_board, [2, 4, 6, 8])
                    if move != None:
                        doMove(game_board, comp_piece, move)


def computer_playerWinCheck(game_board, user_piece):
    for i in range(1, 10):
        copy = boardCopy(game_board)
        if moveCheck(copy, i):
            doMove(copy, user_piece, i)
            if winningCheck(copy, user_piece):
                return i


def computer_win(game_board, comp_piece):
    for i in range(1, 10):
        copy = boardCopy(game_board)
        if moveCheck(copy, i):
            doMove(copy, comp_piece, i)
            if winningCheck(copy, comp_piece):
                return i


def boardCopy(game_board):
    copy_board = []
    for i in game_board:
        copy_board.append(i)
    return copy_board


if __name__ == "__main__":
    heading()
    menu()
    game()
