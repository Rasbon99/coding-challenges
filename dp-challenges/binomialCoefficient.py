""" The following are the common definitions of Binomial Coefficients. 

A binomial coefficient C(n, k) can be defined as the coefficient of x^k in the expansion of (1 + x)^n.

A binomial coefficient C(n, k) also gives the number of ways, disregarding order, that k objects can 
be chosen from among n objects more formally, the number of k-element subsets (or k-combinations) of a n-element set.

The Problem 
Write a function that takes two parameters n and k and returns the value of Binomial Coefficient C(n, k). For example, 
your function should return 6 for n = 4 and k = 2, and it should return 10 for n = 5 and k = 2. 

1) Optimal Substructure 
The value of C(n, k) can be recursively calculated using the following standard formula for Binomial Coefficients.  

   C(n, k) = C(n-1, k-1) + C(n-1, k)
   C(n, 0) = C(n, n) = 1
"""

def solveBinomialCoeff(n, k):
    global memo
    memo = [[0 for _ in range(k+1)] for _ in range(n+1)]
    return binomialCoeff(n, k)

def binomialCoeff(n, k):
    if k > n:
        return 0
    if k == n or k == 0:
        memo[n][k] = 1
        return memo[n][k]
    
    if memo[n][k] != 0:
        return memo[n][k]
    else:
        memo[n][k] = binomialCoeff(n-1, k-1) + binomialCoeff(n-1, k)
        return memo[n][k]
        
    
print(solveBinomialCoeff(10, 4))

#Time Complexity O(n*k)