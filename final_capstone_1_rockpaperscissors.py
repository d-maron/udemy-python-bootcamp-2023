import random

win_moves = [('ROCK', 'SCISSORS'), ('PAPER', 'ROCK'), ('SCISSORS', 'PAPER')]

def player_move():
    choice = ''
    while not choice:
        choose_move = input('What is your move? (1 = ROCK, 2 = PAPER, 3 = SCISSORS, 4 = quit) ').lower()
        if choose_move not in '1234':
            print('*** Please provide a valid input ***')
        else:
            choice = int(choose_move) - 1
            break

    return choice

def computer_move():
    random.seed()
    return random.randint(0,2)


game_on = True
while game_on:

    moveidx = player_move()
    if moveidx == 3:
        game_on = False
        break
    move = win_moves[moveidx][0]
    print(f'Your move: {move} ({moveidx})')
    compmoveidx = computer_move()
    compmove = win_moves[compmoveidx][0]
    print(f'Computer\'s move: {compmove} ({compmoveidx})')

    if move == compmove:
        print('IT\'S A TIE!')
        continue
    elif compmove == win_moves[moveidx][1]:
        print('PLAYER wins!!')
    else:
        print('COMPUTER wins!')


print ('GAME OVER')