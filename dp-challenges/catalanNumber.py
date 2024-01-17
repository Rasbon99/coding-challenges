""" Catalan numbers are defined as a mathematical sequence that consists of positive integers, 
which can be used to find the number of possibilities of various combinations. 

The nth term in the sequence denoted Cn, is found in the following formula: \frac{(2n)!}{((n + 1)! n!)} """

def solveCatalan(n):
    global memo
    memo = [0]*(n+1)
    return cat(n)

def cat(n):
    if n <= 1:
        memo[n] = 1
        return 1
    elif memo[n] != 0:
        return memo[n]
    else:
        for k in range(n):
            memo[n] += cat(k)*cat(n-k-1)
        return memo[n]
    
print(solveCatalan(9))

# Time Coplexity = O(n^2)