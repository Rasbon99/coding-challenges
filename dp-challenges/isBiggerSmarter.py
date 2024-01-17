""" Some people think that the bigger an elephant is, the smarter it is. To disprove this, you want to take
the data on a collection of elephants and put as large a subset of this data as possible into a sequence
so that the weights are increasing, but the IQ’s are decreasing.
Input
The input will consist of data for a bunch of elephants, one elephant per line, terminated by the endof-file. 
The data for a particular elephant will consist of a pair of integers: the first representing its size
in kilograms and the second representing its IQ in hundredths of IQ points. Both integers are between
1 and 10000. The data will contain information for at most 1000 elephants. Two elephants may have
the same weight, the same IQ, or even the same weight and IQ.
Output
Say that the numbers on the i-th data line are W[i] and S[i]. Your program should output a sequence
of lines of data; the first line should contain a number n; the remaining n lines should each contain
a single positive integer (each one representing an elephant). If these n integers are a[1], a[2],..., a[n]
then it must be the case that
W[a[1]] < W[a[2]] < ... < W[a[n]]
and
S[a[1]] > S[a[2]] > ... > S[a[n]]
In order for the answer to be correct, n should be as large as possible. All inequalities are strict:
weights must be strictly increasing, and IQs must be strictly decreasing.
There may be many correct outputs for a given input, your program only needs to find one.
Sample Input
6008 1300
6000 2100
500 2000
1000 4000
1100 3000
6000 2000
8000 1400
6000 1200
2000 1900
Sample Output
4
4
5
9
7 """


def solveIsBiggerSmarter(elefants):
    n = len(elefants)
    memo = [-1]*n
    i = 0
    
    def bANdS(i):

        def isValid(i, j):
            return j == n or elefants[i][0] < elefants[j][0] and elefants[i][1] > elefants[j][1]

        if i == n:
            return 0
        
        if memo[i] != -1:
            return memo[i]
        
        memo[i] = max(bANdS(k) + int(isValid(i, k)) for k in range(i+1, n+1))

        return memo[i]
    
    return bANdS(i)

def solveIsBiggerSmarter2(elefants):
    n = len(elefants)
    memo = [[-1 for _ in range(n+1)] for _ in range(n+1)]
    i, j = 0, 0
    
    def bANdS(i, j):

        if i == n-1 or j == n-1:
            return 0
        
        if memo[i][j] != -1:
            return memo[i][j]
        
        valid = 0
        if elefants[i][0] < elefants[j][0] and elefants[i][1] > elefants[j][1]:
            valid = bANdS(i+1, j+1) + 1

        memo[i][j] = max(valid, bANdS(i, j+1), bANdS(i+1, j))

        return memo[i][j]
    
    return bANdS(i, j)

n = int(input("inserire il n di elefanti: "))

elefants = []
for i in range(n): 
    line = input("inserire il " + str(i+1) + " elefante: ")
    elefants.append(list(map(int, line.strip().split(" "))))

print(solveIsBiggerSmarter2(elefants))

# Time Complexity = O(n^2)














