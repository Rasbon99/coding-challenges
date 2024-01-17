""" Given a binary matrix, find out the maximum size square sub-matrix with all 1s.  """

def solveMatrixOfOnes(matrix):
    rows, cols = len(matrix), len(matrix[0])
    memo = [[-1 for _ in range(cols)] for _ in range(rows)]

    def findSubmatrixs(i,j):
        if i == rows or j == cols:
            return 0
        
        if matrix[i][j] == 0:
            return 0
        
        if memo[i][j] != -1:
            return memo[i][j]
        
        right = findSubmatrixs(i, j+1)
        down = findSubmatrixs(i+1, j)
        diagonal = findSubmatrixs(i+1, j+1)

        memo[i][j] = 1 + min(right, down, diagonal)

        return memo[i][j]
    
    Max = float('-inf')
    for i in range(rows):
        for j in range(cols):
            Max = max(Max, findSubmatrixs(i, j))
    
    return Max ** 2

matrix1 = [
    [1, 0, 1, 0, 0],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0]
]

matrix2 = [
    [0, 1, 1, 0, 1],
    [1, 1, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1]
]

matrix3 = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

print(solveMatrixOfOnes(matrix1))
print(solveMatrixOfOnes(matrix2))
print(solveMatrixOfOnes(matrix3))

# Time Complexity = O(rows * cols)


