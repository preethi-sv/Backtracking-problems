# Problem: Check if path exists from (0,0) to (n-1, n-1) in a nxn maze and
# print the path if exists.


# Print the solution path in the maze
def printSolution(solution):
    for i in solution:
        for j in i:
            print('1' if j == 1 else '.', end='\t')
            # print(str(j) + ' ', end='')
        print()


# Check if moving to position (x, y) is safe and possible
def isSafe(maze, x, y, N):
    return 0 <= x < N and 0 <= y < N and maze[x][y] == 1


# Recursive function to check if Maze problem can be solved, 
# If yes, fills the solution
def solveMaze(maze, x, y, solution, N):
    # if (x, y is goal) return True
    if x == y == N - 1:
        solution[x][y] = 1
        return True

    # Check if maze[x][y] is valid
    if isSafe(maze, x, y, N):
        # mark x, y as part of solution path
        solution[x][y] = 1

        # Move forward in x direction
        if solveMaze(maze, x + 1, y, solution, N):
            return True

        # If moving in x direction doesn't give solution
        # then Move down in y direction
        if solveMaze(maze, x, y + 1, solution, N):
            return True

        # If none of the above movements work then
        # BACKTRACK: un-mark x, y as part of solution path
        solution[x][y] = 0
    return False


# Driver Function
if __name__ == '__main__':
    n = 4
    # Initialising the maze
    mazeBoard = [[1, 0, 0, 0],
                 [1, 1, 1, 1],
                 [0, 1, 0, 1],
                 [1, 1, 1, 1]]

    # Creating a 4 * 4 2-D list
    answer = [[0 for j in range(4)] for i in range(4)]

    if not solveMaze(mazeBoard, 0, 0, answer, n):
        print("Solution doesn't exist")
    else:
        printSolution(answer)
