"""
Suppose you have an NxN chessboard. Determine the number of ways in which it is possible to place N queens so that no pair
of queens can attack each other. Thus, a solution requires that two queens do not share the same row, column, or diagonal 
(assume N > 3).
INPUT
The input consists of several test cases. The first line contains the number of test cases. For each test case, an integer 
representing N is provided.
OUTPUT
For each test case, the program outputs the number of ways to place N queens so that no pair of queens can attack each other.
Note that
Sample Input
3
4
5
8
Sample Output
2
10
92
"""

import numpy as np

global solutions

solutions = []

def nxn_queens(N):
    M = np.zeros((N,N))
    M_old = np.copy(M)
    backtrack([], 0, M, M_old, solutions)



def backtrack(queens, k, M, M_old, solutions):
    c = []
    nc = 0

    if is_a_solution(queens, k, M):
        process_solution(queens, k, M, solutions)
    else:
        k = k+1
        c, nc = construct_candidates(queens, k, M)
        for i in range(nc):
            queens.append(c[i])
            #print(queens)
            M, M_old = make_move(queens, k, M, M_old, c, i)
            backtrack(queens, k, M, M_old, solutions)
            M = unmake_move(queens, k, M, M_old, c, i)
            queens.pop()

def is_a_solution(queens, k, M):
    if len(queens) == M.shape[0]:
        queens_tuple = tuple(sorted(queens))
    
        if queens_tuple not in solutions:
            solutions.append(queens_tuple)
            return True
        

def process_solution(queens, k, M, solutions):
    print(len(solutions))
    #print(solutions)

def construct_candidates(queens, k, M):
    # Prendo solo i valori liberi che sono i possibili in cui posso mettere una nuova regina
    N = M.shape[0]
    c = []

    for i in range(N):
        for j in range(N):
            if M[i][j] == 0:
                c.append((i,j))
    nc = len(c)
    return c, nc


def make_move(queens, k, M, M_old, c, i):
    row, col = c[i]                 #vediamo se va TODO
    M, M_old = fill_diagonals(row, col, M)
    M = fill_axis(row, col, M)

    return M, M_old

def unmake_move(queens, k, M, M_old, c, i):
    return M_old

def fill_diagonals(row, col, M):
    N = M.shape[0]
    M_old = np.copy(M)

    for i in range(N):
        if 0 <= (row + i) < N and 0 <= (col + i) < N:
            M[row + i, col + i] = 1
        if 0 <= (row - i) < N and 0 <= (col - i) < N:
            M[row - i, col - i] = 1
        if 0 <= (row - i) < N and 0 <= (col + i) < N:
            M[row - i, col + i] = 1
        if 0 <= (row + i) < N and 0 <= (col - i) < N:
            M[row + i, col - i] = 1

    return M, M_old

def fill_axis(row, col, M):
    M[:,col] = 1
    M[row,:] = 1
    M[row, col] = 2

    return M

nxn_queens(8)

# Complexity O(2^(N/3)) perchè approssimativamente il numero di soluzioni solitamente 
# è approssimabile a 2^N/3



