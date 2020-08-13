def printSolution(board, N):
    solution = [0 for _ in range(N)]
    for col in range(N):
        for row in range(N):
            if board[row][col] == 1:
                solution[col] = str(row + 1)
    print('[' + ', '.join(solution) + ']')
    # for i in range(N):
    #     for j in range(N):
    #         print(board[i][j], end=" ")
    #     print()


def isSafe(board, row, col, N):
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


def nQueens(board, col, N):
    if col == N:
        printSolution(board, N)
        return True

    result = False
    for row in range(N):
        if isSafe(board, row, col, N):
            board[row][col] = 1
            result = nQueens(board, col + 1, N) or result
            board[row][col] = 0

    return result


if __name__ == "__main__":
    n = 5
    chessboard = [[0 for _ in range(n)] for _ in range(n)]
    if not nQueens(chessboard, 0, n):
        print('No solution')
    else:
        print()
