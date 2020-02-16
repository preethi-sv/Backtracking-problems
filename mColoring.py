def printSolution(solution):
    print('Assigned colors are: ', end='')
    for color in solution:
        print(color, end=' ')


# Check if adjacent n have the chosen color
def isSafe(n, graph, vertex, color, c):
    for i in range(n):
        if graph[vertex][i] == 1 and color[i] == c:
            return False
    return True


def graphColor(n, graph, m, color, vertex):
    # base case: If all n are assigned a color then
    # return true
    if vertex == n:
        return True

    # Consider this vertex v and try different colors
    for c in range(1, m + 1):
        # Check if assignment of color c to v is fine
        if isSafe(n, graph, vertex, color, c):
            color[vertex] = c
            if graphColor(n, graph, m, color, vertex + 1):
                return True
            # else backtrack
            color[vertex] = 0
    return False
    

if __name__ == "__main__":
    n = 4   # number of vertices
    # '1' indicates the n are adjacent
    graph = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
    m = 4
    color = [0] * n
    if not graphColor(n, graph, m, color, 0):
        print('No solution')
    else:
        printSolution(color)

