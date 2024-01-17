"""
Given a string str and a matrix mat[][] of lowercase English alphabets,
 the task is to find whether the string str appears in the matrix (either row-wise or column-wise). 
"""

import numpy as np

def isSafe (M, string, index, x, y, R, C):
    if x >= 0 and x < R and y >= 0 and y < C and M[x][y] == string[index]:
        return True
    else:
        return False
    
def backtrack(M, x, y, R, C, directionX, directionY, string, tempString, index):
    
    if index == len(string):
        return True
    
    
    for i in range(4):

        newX = x + directionX[i]

        newY = y + directionY[i]

        if isSafe(M, string, index, newX, newY, R, C):
            
            tempString.append(string[index])
        
            if backtrack(M, newX, newY, R, C, directionX, directionY, string, tempString, index+1):
                return True
            
            tempString.pop()
    
    return False

def findFirst(M, value, R, C):
    for i in range(R):
        for j in range(C):
            if M[i][j] == value:
                return i, j
    return -1, -1


def findString(M, string):
    M = np.array(M)
    R, C = M.shape
    string = list(map(str, string.strip()))

    print(M)
    print(str(R)+"x"+str(C))
    print(string)

    directionX = [-1, 0, 1, 0]
    directionY = [ 0, 1, 0,-1]

    value = string[0]

    i, j = findFirst(M, value, R, C)

    if backtrack(M, i, j, R, C, directionX, directionY, string, [M[i][j]], 1):
        print("è presente la stringa nella matrice")
    else:
        print("non è presente la stringa nella matrice")

M = [['D', 'B', 'C'],
     ['E', 'D', 'A'],
     ['D', 'H', 'I']]

string = 'ADE'

findString(M, string)

# Complexity O(n*m*4^(n))