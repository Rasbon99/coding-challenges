"""
Si consideri un labirinto L dato come matrice binaria N*N di blocchi in cui il blocco sorgente è il
blocco più in alto a sinistra, cioè L[0][0] e il blocco di destinazione è il blocco più in basso a destra,
cioè L[N-1][N-1] . Un topo parte da L[0][0] e deve raggiungere la destinazione. Il topo può muoversi
solo in due direzioni: in avanti e in basso. Nella matrice, 0 significa che il blocco è un vicolo cieco e 1
significa che il blocco può essere utilizzato nel percorso. Si scriva un algoritmo di Backtracking per
determinare un percorso dalla sorgente alla destinazione. Il percorso è scritto in una nuova matrice
S delle stesse dimensioni di L, in cui la cella è ‘1’se fa parte del percorso, 0 altrimenti.
INPUT
L’input è costituito da una prima riga che indica il numero di casi di test T. Le righe successive sono
i casi di test. Ogni caso di test inizia con una riga che indica la dimensione di riga e colonna, e segue
poi una matrice che rappresenta il labirinto L.
OUTPUT
Si riporti il numero del caso di test e, a seguire, la matrice risultato S per quel caso di test.
Sample Input
1
4 4
1 0 0 0
1 1 0 1
0 1 0 0
1 1 1 1
Sample Output
1
1 0 0 0
1 1 0 0
0 1 0 0
0 1 1 1
"""

import numpy as np

def find_path(M, n):
    path = []
    backtrack(path, 0, 0, 0, M, n)

def backtrack(path, k, x, y, M, n):
    c = []
    nc = 0

    if is_a_solution(path, k, x, y, M, n):
        process_solution(path, k, M, n)
    else:
        k = k + 1
        c, nc = construct_candidates(path, k, x, y, M, n)
        for i in range(nc):
            path.append(c[i])
            new_x, new_y = c[i]
            backtrack(path, k, new_x, new_y, M, n)
            path.pop()
            
def is_a_solution(path, k, x, y, M, n):
    return x == n-1 and y == n-1

def process_solution(path, k, M, n):
    S = np.zeros((n,n), dtype=int)
    for i in range(len(path)):
        x,y = path[i]
        S[x][y] = 1
    print(S)
        

def construct_candidates(path, k, x, y, M, n):
    c = []

    if k == 1:
        if isSafe(x, y, M, n):
            c.append((x,x))
    else: 
        if isSafe(x+1, y, M, n):
            c.append((x+1,y))
        if isSafe(x, y+1, M, n):
            c.append((x,y+1))
    return c, len(c)
    
def isSafe(x, y, M, n):
    if x >= 0 and x < n and y >= 0 and y < n and M[x][y]:
        return True
            
def input():
    file_path = 'maze.txt'

    with open(file_path, 'r') as file:
        nCase = int(file.readline().strip())
        for _ in range(nCase):
            size = int(file.readline().strip())
            maze = []
            for _ in range(size):
                row = list(map(int, file.readline().strip().split(" ")))
                maze.append(row)
            maze = np.array(maze)
            print(size)
            print(maze)
            find_path(maze, size)

input()


            
                 
                 

