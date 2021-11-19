import random

board={1:' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
b_keys = [k for k,v in board.items()]

print("Welcome to Tic Tac Toe")
def print_board():

    print(f"""
--+---+---
{board[1]} | {board[2]} | {board[3]}
--+---+---
{board[4]} | {board[5]} | {board[6]}
--+---+---
{board[7]} | {board[8]} | {board[9]}
--+---+---
    """)

print_board()


def player():
    print('choose a square by numbers from 1 to 9')
    user=int(input('type a number: \n'))
    if board[user] == ' ':
        board[user] = 'X'
        print_board()
    else:
        try:
            player()
        except RecursionError:
            pass
def reset():
    global board
    for key in board:
        board[key] = ' '
    print_board()

def computer():
    com_num= random.randint(1,9)
    if board[com_num] == ' ':
        print("computer's turn")
        board[com_num] = 'O'
        print_board()
    else:
        try:
            computer()
        except RecursionError:
            pass

is_on = True

def won():
    global is_on
    wins = [(board[1], board[2], board[3]), (board[4], board[5], board[6]), (board[7], board[8], board[9]), (board[1], board[4], board[7]), (board[2], board[5], board[8]), (board[3], board[6], board[9]), (board[1], board[5], board[9]), (board[7], board[5], board[3])]
    for win in wins:
        tup1, tup2, tup3 = win
        if tup1 == tup2 == tup3 == "X":
            print('Hurrraay You win')
            is_on=False
            return is_on
        if tup1 == tup2 == tup3 == "O":
            print('Oh no, Computer wins')
            is_on=False
            return is_on
        else:
            return True


def check_win():
    global is_on
    if board[1] == board[2] == board[3] == 'X':
        print('Wow, You win!')
        is_on = False
        return is_on
    elif board[4] == board[5] == board[6] == 'X':
        print('Wow, You win!')
        is_on = False
        return is_on
    elif board[7] == board[8] == board[9] == 'X':
        print('Wow, You win!')
        is_on = False
        return is_on
    elif board[1] == board[4] == board[7] == 'X':
        print('Wow, You win!')
        is_on = False
        return is_on
    elif board[2] == board[5] == board[8] == 'X':
        print('Wow, You win!')
        is_on= False
        return is_on
    elif board[3] == board[6] == board[9] == 'X':
        print('Wow, You win!')
        is_on = False
        return is_on
    elif board[1] == board[5] == board[9] == 'X':
        print('Wow, You win!')
        is_on = False
        return is_on
    elif board[7] == board[5] == board[3] == 'X':
        print('Wow, You win!')
        is_on = False
        return is_on
    elif board[1] == board[2] == board[3] == 'O':
        print('Ohh, Computer wins!')
        is_on = False
        return is_on
    elif board[4] == board[5] == board[6] == 'O':
        print('Ohh, Computer wins!')
        is_on = False
        return is_on
    elif board[7] == board[8] == board[9] == 'O':
        print('Ohh, Computer wins!')
        is_on = False
        return is_on
    elif board[1] == board[4] == board[7] == 'O':
        print('Ohh, Computer wins!')
        is_on = False
        return is_on
    elif board[2] == board[5] == board[8] == 'O':
        print('Ohh, Computer wins!')
        is_on = False
        return is_on
    elif board[3] == board[6] == board[9] == 'O':
        print('Ohh, Computer wins!')
        is_on = False
        return is_on
    elif board[1] == board[5] == board[9] == 'O':
        print('Ohh, Computer wins!')
        is_on = False
        return is_on
    elif board[7] == board[5] == board[3] == 'O':
        print('Ohh, Computer wins!')
        is_on = False
        return is_on
    else:
        return True


def game():
    x=[]
    for num in b_keys:
        k = board[num]
        x.append(k)
    if ' ' not in x:
        global is_on
        is_on = False

while is_on:
    player()
    if check_win():
        computer()
    game()
    if not check_win():
        replay= input('Do you want a rematch? Y or N: \n')
        if replay.lower() == 'y':
            is_on=True
            reset()
            continue
        else:
            print('Good Game and Goodbye')

