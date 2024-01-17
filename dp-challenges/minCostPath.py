""" Given a cost matrix cost[][] and a position (M, N) in cost[][], write a function that returns cost of 
minimum cost path to reach (M, N) from (0, 0). Each cell of the matrix represents a cost to traverse through 
that cell. The total cost of a path to reach (M, N) is the sum of all the costs on that path (including both 
source and destination). You can only traverse down, right and diagonally lower cells from a given cell, i.e., from a 
given cell (i, j), cells (i+1, j), (i, j+1), and (i+1, j+1) can be traversed. 

Note: You may assume that all costs are positive integers. """

def solveMinCostPath(matrix, i_end, j_end):
    rows, cols = len(matrix), len(matrix[0])
    memo = [[-1 for _ in range(cols)] for _ in range(rows)]
    i, j = 0, 0

    def minCostPath(i, j):
        if i > i_end or j > j_end:
            return float('inf')
        elif i == i_end and j == j_end:
            return matrix[i][j]
        
        if memo[i][j] != -1:
            return memo[i][j]
        
        memo[i][j] = min(minCostPath(i+1, j) + matrix[i][j],
                         minCostPath(i, j+1) + matrix[i][j],
                         minCostPath(i+1, j+1) + matrix[i][j])
        
        return memo[i][j]
    
    return minCostPath(i, j) 

matrix1 = [
  [4, 7, 2],
  [1, 8, 5],
  [9, 3, 6]
]
print(solveMinCostPath(matrix1, 1, 2))

# Time Complexity = O(n*m)