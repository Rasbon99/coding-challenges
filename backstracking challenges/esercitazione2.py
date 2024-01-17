""" 
PROBLEM 2
Consider a completely filled binary tree, with nodes numbered in increasing order from top to bottom and from left to right. 
A certain number of balls are dropped one by one from the root until they reach a leaf node. At each non-terminal node, the ball
goes to the left if the value of the X flag associated with the non-terminal node is false (X = F), or to the right if the flag
is set to true (X = T). Initially, all flags are false; when a ball visits a non-terminal node, it changes the current value 
of the flag, setting it to TRUE if it was FALSE (then continuing its descent to the left), and to FALSE if it was TRUE
(then continuing to the right).
In the example, the first ball will fall into position 8, the second in position 12, the third in position 10, and so on.

Write a program to determine the final stopping position P for each test case. For each test case, the range of two parameters
D and I is as follows:

Consider a series of test cases, for each of which two integer values are provided: a Depth value, which is the maximum depth of 
the tree (e.g., Depth = 4 in the figure), and a second value N indicating the Nth ball that is dropped. (It is also assumed that 
N does not exceed the number of leaf nodes (2^(Depth-1)). Write a program to determine the final position of the Nth ball in the 
tree of depth Depth. (Assume 2 ≤ Depth ≤ 10)

INPUT
The first line of the input indicates the number of test cases T. Subsequently, each line indicates the Depth and N pair.

OUTPUT
Each line should report the final position of the ball.

Sample Input
5
4 2
2 2
8 128
3 4
10 1

Sample Output
12
3
255
7
512
"""

def find_position(A, r, nCount, N):
    if A[r] == 'x':                             # se è arrivato ala fine dell'albero controlla se ha finito con le palline tramite nCount
        nCount = nCount + 1
        if nCount == N:
            return r
        r = find_position(A, 0, nCount, N)      
        
    if A[r] == 'f':                             # se è falso diventa vero e vado a sinistra sapendo che il mio indice è pari a 2*r+1 (parte da 0 l'indice, è come se fosse il doppio se contassimo da 1)
        A[r] = 'v'
        r = find_position(A, 2*r+1, nCount, N)
    elif A[r] == 'v':                           # se è vero diventa falso e vado a destra sapenso che il mio indice è dispari a 2*r+2
        A[r] = 'f'
        r = find_position(A, 2*r+2, nCount, N)
    return r

# Crea un vettore con l'ultimo livello (albero) con tutti x e il resto f
def build_tree(D, N):
    if N > 2**D:
        return 0
    
    leng = (2**(D+1))-1
    A = [None]*leng
    for i in range(2**D):
        A[leng-i-1] = 'x'

    for i in range(leng - 2**D):
        A[i] = 'f'
    
    print(A)
    
    p = find_position(A, 0, 0, N)
    return p+1

p = build_tree(1,2)

print(p)

# Complexity O((2**(D+1))-1 + N*D) = O(2^D + D*N)
 
    