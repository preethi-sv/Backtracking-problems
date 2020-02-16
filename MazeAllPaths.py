def isSafe(row, col, maze, n, visited):
    if -1 < row < n and -1 < col < n and not visited[row][col] and maze[row][col] != 0:
        return True
    return False


# Function to print all the possible
# paths from (0, 0) to (n-1, n-1)
def findPathMaze(row, col, maze, n, path, possiblePaths, visited):
    if not isSafe(row, col, maze, n, visited):
        return

    if row == n - 1 and col == n - 1:
        possiblePaths.append(path)
        return

    # Mark the cell as visited
    visited[row][col] = True

    # Try for all the 4 directions (down, left,
    # right, up) in the given order to get the
    # paths in lexicographical order
    if isSafe(row + 1, col, maze, n, visited):
        path = path + 'D'
        findPathMaze(row + 1, col, maze, n, path, possiblePaths, visited)
        path = path[:-1]

    if isSafe(row, col - 1, maze, n, visited):
        path = path + 'L'
        findPathMaze(row, col - 1, maze, n, path, possiblePaths, visited)
        path = path[:-1]

    if isSafe(row, col + 1, maze, n, visited):
        path = path + 'R'
        findPathMaze(row, col + 1, maze, n, path, possiblePaths, visited)
        path = path[:-1]

    if isSafe(row - 1, col, maze, n, visited):
        path = path + 'U'
        findPathMaze(row - 1, col, maze, n, path, possiblePaths, visited)
        path = path[:-1]

    # Mark the cell as unvisited for other possible paths
    visited[row][col] = False


def printPath(maze, n):
    path = ''
    possiblePaths = []
    visited = [[False for _ in range(n)] for _ in range(n)]
    # Call the utility function to
    # find the valid paths
    findPathMaze(0, 0, maze, n, path, possiblePaths, visited)

    for path in possiblePaths:
        print(path, end=' ')


if __name__ == "__main__":
    maze = [[1, 0, 0, 0],
            [1, 1, 0, 1],
            [1, 1, 0, 0],
            [0, 1, 1, 1]]
    n = len(maze)
    printPath(maze, n)
