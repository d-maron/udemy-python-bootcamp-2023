# Tic Tac Toe game

# Globals
gameOn = True
winner = None
board_space = range(1, 10)
current_player = 0
first_move = 1
current_board = [-1] * 9  # Initialize board with empty cells


def draw_board(first=0):
    print('\n' * 100)  # clear board
    cells_display = []

    if first:
        cells_display = board_space
    else:
        # Convert cell values to game pieces to display
        for i in current_board:
            show = ' '
            if i != -1:
                show = chosenPiece[i]
            cells_display.append(show)

    hline = '---|---|---'
    board = [
        '',
        f' {cells_display[6]} | {cells_display[7]} | {cells_display[8]} ',
        hline,
        f' {cells_display[3]} | {cells_display[4]} | {cells_display[5]} ',
        hline,
        f' {cells_display[0]} | {cells_display[1]} | {cells_display[2]} ',
        '',
    ]

    for row in board:
        print(row)


def choosepiece():
    choice = ''

    while choice.upper() not in ('X', 'O'):
        choice = input("Player 1, please choose 'X' or 'O'.").upper()
    print()
    print(f"Player 1, your mark is '{choice}'. You will go first.")

    if choice == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'


def cell_is_empty(pos):
    return current_board[pos] == -1


def choose_move(player):
    choice = ''
    while choice not in board_space:
        choice = input(
            f"Player {player + 1}, "
            f"choose where to put your mark (1-9) Type Q to quit."
        )
        if choice.isdigit():
            choice = int(choice) - 1
            if choice + 1 in board_space:
                if not cell_is_empty(choice):
                    print(f"Space {choice + 1} is already marked.")
                else:
                    choice = int(choice)
                    break
        elif choice.upper() == 'Q':
            if input('Are you sure you want to quit?').upper() == 'Y':
                return 'Q'

        print("Invalid input. Please choose a number from 1-9.")
        choice = ''

    current_board[choice] = player


def is_won():
    win_patterns = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],  # Horizontals
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],  # Verticals
        [0, 4, 8],
        [2, 4, 6],
    ]  # Diagonals

    for pattern in win_patterns:
        match_count = 0
        for i in pattern:
            if current_board[i] == current_player:
                match_count += 1
            if match_count == 3:
                return current_player
    return None


# Start the game
chosenPiece = choosepiece()

draw_board(1)

while gameOn:
    if choose_move(current_player) == 'Q':
        winner = None
        gameOn = False
        break
    draw_board()
    winner = is_won()
    if winner is not None:
        gameOn = False
    current_player = abs(current_player - 1)  # Switch players

# Game over
if winner is None:
    print('Thank you for playing.')
else:
    print(f'Player {winner + 1} has won the game!')
