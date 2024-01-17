""" 
Given a N*N board with the Knight placed on the first block of an empty board.
Moving according to the rules of chess knight must visit each square exactly once.
Print the order of each cell in which they are visited. 

Input : 
N = 8

Output:
0  59  38  33  30  17   8  63
37  34  31  60   9  62  29  16
58   1  36  39  32  27  18   7
35  48  41  26  61  10  15  28
42  57   2  49  40  23   6  19
47  50  45  54  25  20  11  14
56  43  52   3  22  13  24   5
51  46  55  44  53   4  21  12
"""

import numpy as np

def is_safe (board, x, y, N):
    if x >= 0 and x < N and y >= 0 and y < N and board[x][y] == -1:
        return True
    return False

def backtrack(board, x, y, N, directionX, directionY, step):

    if step == N*N:
        return True
    
    for i in range(8):
        
        newX = x + directionX[i]
        newY = y + directionY[i]

        if is_safe(board, newX, newY, N):

            board[newX][newY] = step

            if backtrack(board, newX, newY, N, directionX, directionY, step+1):
                return True
            
            board[newX][newY] = -1

    return False


    

def solve_knight(N):

    board = np.full((N,N), -1)
    board[0][0] = 0

    directionX = [-1,-2,-2,-1, 1, 2, 2, 1]
    directionY = [-2,-1, 1, 2,-2,-1, 1, 2]

    if backtrack(board, 0, 0, N, directionX, directionY, 1):
        print(board)
    else:
        print("Non ci sono soluzioni")


def process_input():

    with open("knight.txt", 'r') as file:

        n = int(file.readline().strip())

        print(str(n) + "x" + str(n))

        solve_knight(n)

process_input()

# Complexity O(8^(n*n))