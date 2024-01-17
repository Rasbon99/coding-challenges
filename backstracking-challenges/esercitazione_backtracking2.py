"""
Longest Run on a Snowboard
Michael likes snowboarding. That’s not very surprising, since snowboarding is really great. The bad
thing is that in order to gain speed, the area must slide downwards. Another disadvantage is that when
you’ve reached the bottom of the hill you have to walk up again or wait for the ski-lift.
Michael would like to know how long the longest run in an area is. That area is given by a grid of
numbers, defining the heights at those points. Look at this example:
1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
One can slide down from one point to a connected other one if and only if the height decreases. One
point is connected to another if it’s at left, at right, above or below it. In the sample map, a possible
slide would be 24-17-16-1 (start at 24, end at 1). Of course if you would go 25-24-23-…-3-2-1, it would
be a much longer run. In fact, it’s the longest possible.

Input
The first line contains the number of test cases N. Each test case starts with a line containing the
name (it’s a single string), the number of rows R and the number of columns C. After that follow R
lines with C numbers each, defining the heights. R and C won’t be bigger than 100, N not bigger than
15 and the heights are always in the range from 0 to 100.

Output
For each test case, print a line containing the name of the area, a colon, a space and the length of the
longest run one can slide down in that area.
Sample Input
2
Feldberg 10 5
56 14 51 58 88
26 94 24 39 41
24 16 8 51 51
76 72 77 43 10
38 50 59 84 81
5 23 37 71 77
96 10 93 53 82
94 15 96 69 9
74 0 62 38 96
37 54 55 82 38
Spiral 5 5
1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9

Sample Output
Feldberg: 7
Spiral: 25
"""
import numpy as np

# Guarda attorno ai possibili passi, passa i passi con distanza minore se esistono
def short_distance(slope, x, y, steps, nSteps, shortest):
    resShortest = []
    for i in range(nSteps):
        nextX, nextY = steps[i]

        if slope[x][y] >= slope[nextX][nextY]:
            distance = abs(slope[x][y] - slope[nextX][nextY])

            if distance < shortest:
                shortest = distance
                resShortest = [(nextX, nextY)]
            elif distance == shortest:
                resShortest.append((nextX, nextY))

    return resShortest
            

def is_safe(x, y, R, C):
    if x >= 0 and x < R and y >= 0 and y < C:
        return True
    return False

def backtrack(slope, x, y, startX, startY, directionX, directionY, R, C, runs, startDistance):

    if x == R-1 and y == C-1:
        return True
    
    steps = []
    nSteps = 0
    
    # costruisco i possibili candidati
    for i in range(4):

        newX = x + directionX[i]
        newY = y + directionY[i]

        if is_safe(newX, newY, R, C):
            nSteps += 1
            steps.append((newX, newY))
    
    shortest = short_distance(slope, x, y, steps, nSteps, 101)
    print(shortest)

    if shortest:
        # Lista piena
        for step in shortest:
            nextX, nextY = step

            startDistance += slope[nextX][nextY]
            runs[startX][startY] = startDistance

            if backtrack(slope, nextX, nextY, startX, startY, directionX, directionY, R, C, runs, startDistance):
                return True
    else:
        # Lista vuota
        
        for i in range(R):
            for j in range(C):
                if runs[i][j] == -1 and backtrack(slope, 0, 0, i, j, directionX, directionY, R, C, runs, 0):
                    return True
                
    return False


def find_longest_list(slope, R, C):
    runs = np.full((R,C), -1)
    
    directionX = [-1,1,0,0]
    directionY = [0,0,-1,1]

    if backtrack(slope, 0, 0, 0, 0, directionX, directionY, R, C, runs, 0):
        print(runs)
    else:
        print("Non ci sono soluzioini")
    

def process_input():
    file_path = 'snowboard.txt'

    with open(file_path, 'r') as file:
        nCase = int(file.readline().strip())
        linea = file.readline().strip().split(" ")

        stringa = linea[0]
        R = int(linea[1])
        C = int(linea[2])
        
        for _ in range(nCase):
            M = []
            for _ in range(R):
                row = list(map(int, file.readline().strip().split(" ")))
                M.append(row)
            M = np.array(M)
            print(stringa)
            print(str(R) + " " +str(C))
            print(M)
            find_longest_list(M, R, C)

process_input()

