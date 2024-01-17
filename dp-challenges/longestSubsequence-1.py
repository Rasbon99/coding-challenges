""" Given an array of n size, the task is to find the longest subsequence such that difference between adjacents is one. 

Examples: 

Input :  arr[] = {10, 9, 4, 5, 4, 8, 6}
Output :  3
As longest subsequences with difference 1 are, "10, 9, 8", 
"4, 5, 4" and "4, 5, 6"

Input :  arr[] = {1, 2, 3, 2, 3, 7, 2, 1}
Output :  7
As longest consecutive sequence is "1, 2, 3, 2, 3, 2, 1" """

def solveLSD(seq):
    n = len(seq)
    memo = [[0 for _ in range(n+1)] for _ in range (n+1)]
    i = 0
    prec = -1
    
    def LSD(i, prec):
        
        def is_one(i, j):
            return j == n or ((abs(seq[i] - seq[j])) == 1)
        
        if i == n:
            return 0
        
        if memo[i][prec] != 0:
            return memo[i][prec]
        
        memo[i][prec] = max(LSD(j, i) + int(is_one(i, j)) for j in range(i+1, n+1))

        return memo[i][prec]
    
    return LSD(i, prec)

print(solveLSD([10, 9, 4, 5, 4, 8, 6]))

# Time complexity = O(n^2)