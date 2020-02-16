def printSolution(board):
    solution = [0 for i in range(N)]
    for col in range(N):
        for row in range(N):
            if board[row][col] == 1:
                solution[col] = str(row + 1)
    strSol = '[' + ' '.join(solution) + ']'
    print(strSol, end=' ')
    # for i in range(N):
    #     for j in range(N):
    #         print(board[i][j], end=" ")
    #     print()


def isSafe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def nQueens(board, col):
    if col == N:
        printSolution(board)
        return True

    result = False
    for row in range(N):
        if isSafe(board, row, col):
            board[row][col] = 1
            result = nQueens(board, col + 1) or result
            board[row][col] = 0

    return result


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        N = int(input())
        board = [[0 for _ in range(N)] for _ in range(N)]
        if not nQueens(board, 0):
            print('-1')
        else:
            print()
