import random

win_moves = [('ROCK', 'SCISSORS'), ('PAPER', 'ROCK'), ('SCISSORS', 'PAPER')]
score = {'You': 0, 'Computer': 0}

def player_move():
    choice = ''
    while not choice:
        choose_move = input('What is your move? (1 = ROCK, 2 = PAPER, 3 = SCISSORS, 4 = quit) ').lower()
        if choose_move not in [str(i) for i in range(1,4)]:
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
    print(f'Your move: {move}')
    compmoveidx = computer_move()
    compmove = win_moves[compmoveidx][0]
    print(f'Computer\'s move: {compmove}')

    if move == compmove:
        print('IT\'S A TIE!')
    elif compmove == win_moves[moveidx][1]:
        print('PLAYER wins!!')
        score['You'] += 1
    else:
        print('COMPUTER wins!')
        score['Computer'] += 1

    print(f'SCORE:')
    for i in score.keys():
        print('  ', i, score[i])

print ('GAME OVER')