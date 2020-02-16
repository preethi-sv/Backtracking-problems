global N
N = 4


def printSolution(sol):
    for i in sol:
        for j in i:
            print(str(j) + " ", end="")
        print("")


def isSafe(maze, x, y):
    if 0 <= x < N and 0 <= y < N and maze[x][y] == 1:
        return True

    return False


# A recursive utility function to solve Maze problem
def solveMaze(maze, x, y, sol):
    # if (x, y is goal) return True
    if x == y == N - 1:
        sol[x][y] = 1
        return True

    # Check if maze[x][y] is valid
    if isSafe(maze, x, y):
        # mark x, y as part of solution path
        sol[x][y] = 1

        # Move forward in x direction
        if solveMaze(maze, x + 1, y, sol):
            return True

        # If moving in x direction doesn't give solution
        # then Move down in y direction
        if solveMaze(maze, x, y + 1, sol):
            return True

        # If none of the above movements work then
        # BACKTRACK: unmark x, y as part of solution path
        sol[x][y] = 0
        return False


if __name__ == "__main__":
    # Initialising the maze
    maze = [[1, 0, 0, 0],
            [1, 1, 0, 1],
            [0, 1, 0, 0],
            [1, 1, 1, 1]]

    # Creating a 4 * 4 2-D list
    sol = [[0 for j in range(4)] for i in range(4)]

    if not solveMaze(maze, 0, 0, sol):
        print("Solution doesn't exist")
    else:
        printSolution(sol)
