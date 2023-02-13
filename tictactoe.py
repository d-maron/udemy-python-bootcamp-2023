# Tic Tac Toe game

# Globals
gameOn = True
winner = None
boardSpace = range(1, 10)
currentPlayer = 0
firstMove = 1
currentBoard = [-1] * 9  # Initialize board with empty cells


def drawBoard(firstMove=0):
    print('\n' * 100)  # clear board
    dispCells = []

    if firstMove:
        dispCells = boardSpace
        firstMove = 0
    else:
        # Convert cell values to game pieces to display
        for i in currentBoard:
            show = ' '
            if i != -1:
                show = chosenPiece[i]
            dispCells.append(show)

    hLine = '---|---|---'
    board = [
        '',
        f' {dispCells[6]} | {dispCells[7]} | {dispCells[8]} ',
        hLine,
        f' {dispCells[3]} | {dispCells[4]} | {dispCells[5]} ',
        hLine,
        f' {dispCells[0]} | {dispCells[1]} | {dispCells[2]} ',
        '',
    ]

    for row in board:
        print(row)


def choosePiece():
    choice = ''

    while choice.upper() not in ('X', 'O'):
        choice = input("Player 1, please choose 'X' or 'O'.").upper()
    print()
    print(f"Player 1, your mark is '{choice}'. You will go first.")

    if choice == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def cellIsEmpty(pos):
    return currentBoard[pos] == -1


def chooseMove(player):
    choice = ''
    while choice not in boardSpace:
        choice = input(
            f"Player {player+1}, "
            f"choose where to put your mark (1-9) Type Q to quit."
        )
        if choice.isdigit():
            choice = int(choice) - 1
            if choice + 1 in boardSpace:
                if not cellIsEmpty(choice):
                    print(f"Space {choice+1} is already marked.")
                else:
                    choice = int(choice)
                    break
        elif choice.upper() == 'Q':
            if input('Are you sure you want to quit?').upper() == 'Y':
                return 'Q'

        print("Invalid input. Please choose a number from 1-9.")
        choice = ''

    currentBoard[choice] = player


def isWon():
    winPatterns = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],  # Horizontals
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],  # Verticals
        [0, 4, 8],
        [2, 4, 6],
    ]  # Diagonals

    for pattern in winPatterns:
        matchCount = 0
        for i in pattern:
            if currentBoard[i] == currentPlayer:
                matchCount += 1
            if matchCount == 3:
                return currentPlayer
    return None


# Start the game
chosenPiece = choosePiece()

drawBoard(1)

while gameOn:
    if chooseMove(currentPlayer) == 'Q':
        winner = None
        gameOn = False
        break
    drawBoard()
    winner = isWon()
    if winner is not None:
        gameOn = False
    currentPlayer = abs(currentPlayer - 1)  # Switch players

# Game over
if winner is None:
    print('Thank you for playing.')
else:
    print(f'Player {winner+1} has won the game!')
