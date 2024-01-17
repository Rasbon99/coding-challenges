""" The problem is to count all unique possible paths from the top left to the bottom right of a M X N 
matrix with the constraints that from each cell you can either move only to the right or down.

Examples: 

Input:  M = 2, N = 2
Output: 2
Explanation: There are two paths
(0, 0) -> (0, 1) -> (1, 1)
(0, 0) -> (1, 0) -> (1, 1)

Input:  M = 2, N = 3
Output: 3
Explanation: There are three paths
(0, 0) -> (0, 1) -> (0, 2) -> (1, 2)
(0, 0) -> (0, 1) -> (1, 1) -> (1, 2)
(0, 0) -> (1, 0) -> (1, 1) -> (1, 2) """

def solveCountPath(rows, cols):
    memo = [[-1 for _ in range(cols+1)] for _ in range(rows+1)]
    i, j = 0, 0

    def countPaths(i, j):
        if i == rows-1 and j == cols-1:
            return 1
        if i > rows or j > cols:
            return 0
        
        if memo[i][j] != -1:
            return memo[i][j]
        
        memo[i][j] = countPaths(i+1, j) + countPaths(i, j+1)

        return memo[i][j]
    
    return countPaths(i, j)

print(solveCountPath(2, 3))

# Time Complexity = O(n*m)