# Problem: Check if the given sudoku board can be solved and print solution if exists.

# Print the solution
def printGrid(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=' ')
        print()


# Check if an empty location is found in board
# If so, fill location with row and col of empty location
def findEmptyLocation(board, location):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                location[0] = row
                location[1] = col
                return True
    return False


# Check if number num is used in given row
def usedInRow(board, row, num):
    for i in range(9):
        if board[row][i] == num:
            return True
    return False


# Check if number num is used in given column col
def usedInColumn(board, col, num):
    for i in range(9):
        if board[i][col] == num:
            return True
    return False


# Check if number num is used in the 3 x 3 box starting at (row, col)
def usedInBox(board, row, col, num):
    for i in range(3):
        for j in range(3):
            if board[i + row][j + col] == num:
                return True
    return False


# Check if it is safe to assign number num to the location at (row, col)
def isLocationSafe(board, row, col, num):
    return not usedInRow(board, row, num) and not usedInColumn(board, col, num) \
           and not usedInBox(board, row - row % 3, col - col % 3, num)


# Function that checks if the sudoku board can be solved,
# If possible, fill the board with solution
def solveSudoku(board):
    location = [0, 0]

    # if an empty location is found, l contains its row and col number
    if not findEmptyLocation(board, location):
        return True
    row, col = location

    for num in range(1, 10):
        if isLocationSafe(board, row, col, num):
            # make tentative assignment
            board[row][col] = num
            # return, if success, ya!
            if solveSudoku(board):
                return True
            # failure, unmake & try again
            board[row][col] = 0

    # this triggers backtracking
    return False


# Driver function
if __name__ == "__main__":
    
    # assigning values to the 9x9 grid
    # grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
    #         [5, 2, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 8, 7, 0, 0, 0, 0, 3, 1],
    #         [0, 0, 3, 0, 1, 0, 0, 8, 0],
    #         [9, 0, 0, 8, 6, 3, 0, 0, 5],
    #         [0, 5, 0, 0, 9, 0, 6, 0, 0],
    #         [1, 3, 0, 0, 0, 0, 2, 5, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 7, 4],
    #         [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    grid = [[8, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 3, 6, 0, 0, 0, 0, 0],
            [0, 7, 0, 0, 9, 0, 2, 0, 0],
            [0, 5, 0, 0, 0, 7, 0, 0, 0],
            [0, 0, 0, 0, 4, 5, 7, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 3, 0],
            [0, 0, 1, 0, 0, 0, 0, 6, 8],
            [0, 0, 8, 5, 0, 0, 0, 1, 0],
            [0, 9, 0, 0, 0, 0, 4, 0, 0]]

    # if success print the grid
    if solveSudoku(grid):
        printGrid(grid)
    else:
        print("No solution exists")
