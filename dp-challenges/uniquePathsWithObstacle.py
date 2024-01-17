""" Given a grid of size m * n, let us assume you are starting at (1, 1) and your goal is to reach (m, n). 
At any instance, if you are on (x, y), you can either go to (x, y + 1) or (x + 1, y).
Now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and space are marked as 1 and 0 respectively in the grid.

Examples:  

Input: [[0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]]

Output: 2 """

def solveUniquePath(matrix):
    rows, cols = len(matrix), len(matrix[0])
    memo = [[-1 for _ in range(cols)] for _ in range(rows)]
    i, j = 0, 0

    def uniquePaths(i, j):
        if i == rows-1 and j == cols-1:
            return 1
        if i > rows-1 or j > cols-1:
            return 0
        
        if memo[i][j] != -1:
            return memo[i][j]
        
        count_1, count_2 = 0, 0
        if (i+1 <= rows-1) and not matrix[i+1][j]:
            count_1 = uniquePaths(i+1, j)
        if (j+1 <= cols-1) and not matrix[i][j+1]:
            count_2 = uniquePaths(i, j+1)

        memo[i][j] = count_1 + count_2

        return memo[i][j]
    
    return uniquePaths(i, j)

matrix = [[0, 0, 0],
          [0, 1, 0],
          [0, 0, 0]]

print(solveUniquePath(matrix))

# Time Complexity = o(n*m)

    
    