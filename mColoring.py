# Problem: Given adjacency matrix of a graph, check if the graph vertices 
# can be colored with m colors. Print solution if exists.


# Print the colors assigned
def printSolution(solution):
    print('Assigned colors are: ', end='')
    for color in solution:
        print(color, end=' ')


# Check if adjacent vertices have the chosen color
def isSafe(n, graph, vertex, color, c):
    for i in range(n):
        if graph[vertex][i] == 1 and color[i] == c:
            return False
    return True


# Check if m colors can be sufficient to color a graph,
# if yes assign the colors
def graphColor(n, graph, m, color, vertex):
    # base case: If all n vertices are assigned a color then
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
    

# Driver Function
if __name__ == "__main__":
    N = 4   # number of vertices
    # '1' indicates the n are adjacent
    Graph = [[0, 1, 1, 1],
             [1, 0, 1, 0],
             [1, 1, 0, 1],
             [1, 0, 1, 0]]
    M = 4
    Color = [0] * N
    if not graphColor(N, Graph, M, Color, 0):
        print('No solution')
    else:
        printSolution(Color)

