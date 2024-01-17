""" Given two strings, S1 and S2, the task is to find the length of the Longest Common Subsequence,
i.e. longest subsequence present in both of the strings. 

A longest common subsequence (LCS) is defined as the longest subsequence which is common in all given input sequences. """

def solveLCS(s1, s2):
    n = len(s1)
    m = len(s2)
    memo = [[0 for _ in range(m+1)] for _ in range(n+1)]
    i, j = 0, 0

    def LCS(i, j):

        if i == n or j == m:
            return 0

        if memo[i][j] != 0:
            return memo[i][j]
        
        equal = 0
        if s1[i] == s2[j]:
            equal = LCS(i+1, j+1) + 1

        memo[i][j] = max(equal, LCS(i+1, j), LCS(i, j+1))

        return memo[i][j]
    
    return LCS(i, j)

print(solveLCS("AGGTAB", "GXTXAYB"))

# Time Complexity = O(n*m)