# Problem: Check if N Queens can be placed safely in a board
# Print solution if exists 

# Function to print the board with N Queens
def printSolution(board, N):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                print('Q' + str(i+1), end='\t')
            else:
                print('.', end='\t')
        print()
    # Solution as n-tuple
    print(', '.join([str(j+1) for i in range(N) for j in range(N) if board[i][j]]))


# Function to check if placing queen at board[row][col] is safe
def isSafe(board, row, col, N):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


# Function to solve N Queens problem
def solveNQueens(board, col, N):
    # base case: If all queens are placed then return true 
    if col == N:
        return True

    # Consider this column and try placing 
    # this queen in all rows one by one 
    for i in range(N):
        if isSafe(board, i, col, N):
            # Place this queen in board[i][col] 
            board[i][col] = 1
            # recur to place rest of the queens
            if solveNQueens(board, col + 1, N):
                return True
            # If placing queen in board[i][col] doesn't lead to a solution, then 
            # queen from board[i][col] 
            board[i][col] = 0

    # if the queen can not be placed in any row in 
    # this column col then return false 
    return False


if __name__ == "__main__":
    n = 4
    chessboard = [[0 for i in range(n)] for j in range(n)]
    # If solution exists
    if solveNQueens(chessboard, 0, n):
        printSolution(chessboard, n)
    else:
        print("Solution does not exist")
