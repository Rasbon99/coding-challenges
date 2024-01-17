"""
Consider a maze L given as an N*N binary matrix of blocks where the source block is the top-left block, i.e., L[0][0], 
and the destination block is the bottom-right block, i.e., L[N-1][N-1]. A mouse starts from L[0][0] and needs to reach 
the destination. The mouse can only move in two directions: forward and downward. In the matrix, 0 indicates that the block 
is a dead end, and 1 means the block can be used in the path. Write a Backtracking algorithm to determine a path from the source 
to the destination. The path is written in a new matrix S of the same dimensions as L, where the cell is '1' if it is part of the path,
 0 otherwise.

INPUT:
The input consists of a first line indicating the number of test cases T. The subsequent lines are the test cases. Each test case
 begins with a line indicating the row and column dimensions, followed by a matrix representing the maze L.

OUTPUT:
Report the test case number and, below it, the resulting matrix S for that test case.

Sample Input:
1
4 4
1 0 0 0
1 1 0 1
0 1 0 0
1 1 1 1

Sample Output:
1
1 0 0 0
1 1 0 0
0 1 0 0
0 1 1 1
"""

import numpy as np

def is_safe(maze, x, y, n, exitPath):
    if x >= 0 and x < n and y >= 0 and y < n and maze[x][y] == 1 and exitPath[x][y] == 0:
        return True
    return False

def backtrack(maze, x, y, directionX, directionY, n, exitPath):

    # Verifico subito se è una soluzione globale, in questo caso ritorna backtrack
    if x == n-1 and y == n-1:
        return True
    
    for i in range(2):
        
        # Nuovo candidato della x
        newX = x + directionX[i]

        # Nuovo candidato della y
        newY = y + directionY[i]

        if is_safe(maze, newX, newY, n, exitPath):

            # Se è uno stato valido lo aggiungo al mio exit path
            exitPath[newX][newY] = 1

            # Avanzo su questo stato, se i backtrack successivi mi passano true vuol dire che ho trovato la soluzione e salgo
            if backtrack(maze, newX, newY, directionX, directionY, n, exitPath):
                return True
            
            # Non ha portato a nuove soluzioni dunque lo elimino
            exitPath[newX][newY] = 0

    return False
    
def find_exit(maze, n):
    exitPath = np.zeros((n,n))
    
    # Imposto il punto di partenza
    exitPath[0][0] = 1

    # Possibilil direzioni (x+1,y) e (x,y+1)
    directionX = [1, 0]

    directionY = [0, 1]

    if backtrack(maze, 0, 0, directionX, directionY, n, exitPath):
        print(exitPath)
    else:
        print("Non esistono soluzioni")


def input():

    with open("maze.txt", 'r') as file:

        nCase = int(file.readline().strip())

        data = []

        for _ in range(nCase):
            n = int(file.readline().strip())

            for _ in range(n):
                data.append(list(map(int,file.readline().strip().split(" "))))

            maze = np.array(data)

            print(str(n) + "x" + str(n))
            print(maze)

            find_exit(maze, n)

input()

# Complexity O(2^(n+m))