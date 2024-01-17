""" Given three numbers n, r and p, compute value of nCr mod p. 
Example: 

Input:  n = 10, r = 2, p = 13
Output: 6
Explanation: 10C2 is 45 and 45 % 13 is 6. """

def solve_nCrmodP(n, k, p):
    global memo
    memo = [[0 for _ in range(k+1)] for _ in range(n+1)]
    return binomialCoeff(n, k) % p

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
        
    
print(solve_nCrmodP(10, 2, 13))

#Time Complexity O(n*k)