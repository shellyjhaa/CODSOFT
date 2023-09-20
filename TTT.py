board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('\n')

def spaceIsFree(position):
    return board[position] == ' '

def checkForWin():
    # Check rows
    for i in range(1, 8, 3):
        if board[i] == board[i + 1] == board[i + 2] != ' ':
            return True
    # Check columns
    for i in range(1, 4):
        if board[i] == board[i + 3] == board[i + 6] != ' ':
            return True
    # Check diagonals
    if board[1] == board[5] == board[9] != ' ':
        return True
    if board[3] == board[5] == board[7] != ' ':
        return True
    return False

def checkDraw():
    return ' ' not in board.values()

def insertLetter(letter, position):
    if spaceIsFree(position):
        board[position] = letter
        printBoard(board)
        if checkDraw():
            print("Draw!")
            exit()
        if checkForWin():
            if letter == 'X':
                print("Player wins!")
            else:
                print("Bot wins!")
            exit()
    else:
        print("Can't insert there!")
        position = int(input("Enter new position: "))
        insertLetter(letter, position)

def main():
    while True:
        printBoard(board)
        insertLetter("X", int(input("Enter your move (1-9): ")))
        insertLetter("O", findBestMove())

def findBestMove():
    best_score = -float('inf')
    best_move = None

    for i in range(1, 10):
        if spaceIsFree(i):
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '

            if score > best_score:
                best_score = score
                best_move = i

    return best_move

def minimax(board, depth, is_maximizing):
    if checkForWin():
        return 1 if is_maximizing else -1
    elif checkDraw():
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(1, 10):
            if spaceIsFree(i):
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(1, 10):
            if spaceIsFree(i):
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

if __name__ == "__main__":
    main()
