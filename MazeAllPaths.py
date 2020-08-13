def isSafe(row, col, maze, n, visited):
    if 0 <= row < n and 0 <= col < n and not visited[row][col] and maze[row][col] != 0:
        return True
    return False


def printCurrentPath(path):
    possiblePaths.append(path)
    print(path, end=' ')


# Function to print all the possible paths from (0, 0) to (n-1, n-1)
def findPathMaze(row, col, maze, n, path, visited):

    if row == col == n - 1:
        printCurrentPath(path)
        return

    if isSafe(row, col, maze, n, visited):
        # Mark the cell as visited
        visited[row][col] = True

        # Try for all the 4 directions (down, left, right, up) in the given 
        # order to get the paths in lexicographical order
        if isSafe(row + 1, col, maze, n, visited):
            findPathMaze(row + 1, col, maze, n, path + 'D', visited)
            # Since we are not changing path in this scope,
            # we need not un mark the change we do to backtrack
            # The above line is similar to
            # path = path + 'D'
            # findPathMaze(path + 'D')
            # path = path[:-1]

        if isSafe(row, col - 1, maze, n, visited):
            findPathMaze(row, col - 1, maze, n, path + 'L', visited)

        if isSafe(row, col + 1, maze, n, visited):
            findPathMaze(row, col + 1, maze, n, path + 'R', visited)

        if isSafe(row - 1, col, maze, n, visited):
            findPathMaze(row - 1, col, maze, n, path + 'U', visited)

        # Mark the cell as unvisited for other possible paths
        visited[row][col] = False

    return


if __name__ == "__main__":

    Maze = [[1, 0, 0, 0],
            [1, 1, 0, 1],
            [1, 1, 0, 0],
            [0, 1, 1, 1]]

    N = len(Maze)
    possiblePaths = []
    Visited = [[False for _ in range(N)] for _ in range(N)]

    # findPathMaze(row, col, maze, n, path, visited)
    findPathMaze(0, 0, Maze, N, '', Visited)
    if len(possiblePaths) == 0:
        print('No path exists!')
