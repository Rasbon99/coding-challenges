"""
Print all possible paths from the top-left to the bottom-right of an mXn matrix with the constraint 
that you can only move right or down from each cell.
Examples
INPUT
1 2 3
4 5 6
OUTPUT
1 4 5 6
1 2 5 6
1 2 3 6
INPUT
1 2
3 4
OUTPUT
1 2 4
1 3 4
"""

import numpy as np

def find_paths(m,n):
    M = np.zeros((m,n))
    iteration = 1
    for i in range(m):
        for j in range(n):
            M[i][j] = iteration
            iteration = iteration + 1
    print(M)
    backtrack([], 0, M, 0, 0)

def backtrack(a, k, M, row, col):       # a = soluzione, k = livello, M = matrice da esplorare, row = righe, col = colonne
    c = []                              # ci sono solo due possibili direzioni, quindi tiene conto delle coordinate del prossimo passo
    nc = 0

    if is_a_solution(a, k, M, row, col):
        process_solution(a, k, M, row, col)
    else:
        k = k + 1
        c, nc = construct_candidates(a, k, M, row, col)
        for i in range(nc):
            a.append(c[i])
            newRow, newCol = c[i]
            backtrack(a, k, M, newRow, newCol)
            a.pop()

def construct_candidates(a, k, M, row, col):
    m, n = np.shape(M)
    c = []
    if row == 0 and col == 0:
        a.append((0, 0))
    if row < m - 1:
        c.append((row + 1, col))
    if col < n - 1:
        c.append((row, col + 1))
    nc = len(c)
    return c, nc

def is_a_solution(a, k, M, row, col):
    m,n = np.shape(M)
    return row == m-1 and col == n-1

def process_solution(a, k, M, row, col):
    output = [M[row][col] for (row, col) in a]
    print(output)

find_paths(5,5)


# Complexity O(2^(n+m))