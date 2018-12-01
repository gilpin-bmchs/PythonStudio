EMPTY_SPACE = '.'
X_PLAYER = 'X'
O_PLAYER = 'O'

def drawBoard(board):
    tileChars = []
    for y in range(6):
        for x in range(7):
            tileChars.append(board[(x, y)])

    print("""
+-------+
|{}{}{}{}{}{}{}|
|{}{}{}{}{}{}{}|
|{}{}{}{}{}{}{}|
|{}{}{}{}{}{}{}|
|{}{}{}{}{}{}{}|
|{}{}{}{}{}{}{}|
+-------+
 0123456""".format(*tileChars))


def getNewBoard():
    # Note: The board is 7x6, represented by a dictionary with keys
    # of (x, y) tuples from (0, 0) to (6, 5), and values of '.' (empty),
    # 'X' (X player), or 'O' (O player)
    board = {}
    for y in range(6):
        for x in range(7):
            board[(x, y)] = EMPTY_SPACE
    return board


def getPlayerMove(playerTile, board):
    while True:
        print('Enter your move (0-6):')
        move = input()
        if move not in '0123456':
            continue # Ask again for their move.

        move = int(move)

        for i in range(5, -1, -1):
            if board[(move, i)] == EMPTY_SPACE:
                return (move, i)


def isFull(board):
    for y in range(6):
        for x in range(7):
            if board[(x, y)] != EMPTY_SPACE:
                return False
    return True


def isWinner(playerTile, board):
    b = board # Using a shorter name instead of `board`.

    # Go through the entire board, checking for four-in-a-row.
    for y in range(2):
        for x in range(3):
            # Check for four-in-a-row going across:
            if b[(x, y)] == b[(x + 1, y)] == b[(x + 2, y)] == b[(x + 3, y)] == playerTile:
                return True

            # Check for four-in-a-row going down:
            if b[(x, y)] == b[(x, y + 1)] == b[(x, y + 2)] == b[(x, y + 3)] == playerTile:
                return True

            # Check for four-in-a-row going right-down diagonal:
            if b[(x, y)] == b[(x + 1, y + 1)] == b[(x + 2, y + 2)] == b[(x + 3, y + 3)] == playerTile:
                return True

            # Check for four-in-a-row going left-down diagonal:
            if b[(x + 3, y)] == b[(x + 2, y + 1)] == b[(x + 1, y + 2)] == b[(x, y + 3)] == playerTile:
                return True
    return False


def main():
    gameBoard = getNewBoard()
    playerTurn = X_PLAYER

    while True:
        drawBoard(gameBoard)

        playerMove = getPlayerMove(playerTurn, gameBoard)
        gameBoard[playerMove] = playerTurn

        if isWinner(playerTurn, gameBoard):
            print('Player %s has won!' % (playerTurn))
            break
        elif isFull(gameBoard):
            print('There is a tie!')
            break

        if playerTurn == X_PLAYER:
            playerTurn = O_PLAYER
        elif playerTurn == O_PLAYER:
            playerTurn = X_PLAYER


if __name__ == '__main__':
    main()
