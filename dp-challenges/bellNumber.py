""" Given a set of n elements, find number of ways of partitioning it. 

Input:  n = 2
Output: Number of ways = 2
Explanation: Let the set be {1, 2}
            { {1}, {2} } 
            { {1, 2} }
Input:  n = 3
Output: Number of ways = 5
Explanation: Let the set be {1, 2, 3}
             { {1}, {2}, {3} }
             { {1}, {2, 3} }
             { {2}, {1, 3} }
             { {3}, {1, 2} }
             { {1, 2, 3} }. 

What is a Bell Number? 
Let S(n, k) be total number of partitions of n elements into k sets. The value of n’th Bell Number is sum of S(n, k) for k = 1 to n. 
Bell(n) = \sum_{k=1}^{n}S(n,k)                            
Value of S(n, k) can be defined recursively as, S(n+1, k) = k*S(n, k) + S(n, k-1) """

import math as m

def solveBell(n):
    global memo
    memo = [[0 for _ in range(n+1)] for _ in range(n+1)]
    return bell(n, n-1)

def bell(n, k):
    if k > n:
        return 0
    elif n == 0 or k == 0:
        return 0
    elif n == k:
        memo[n][k]= 1
        return memo[n][k]
    
    elif memo[n][k] != 0:
        return memo[n][k]
    else:
        memo[n][k] = k*bell(n-1, k) + bell(n-1, k-1)
        return memo[n][k]
    
print(solveBell(4))