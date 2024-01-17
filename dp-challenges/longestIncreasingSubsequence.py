""" Given an array arr[] of size N, the task is to find the length of the Longest Increasing Subsequence (LIS) 
i.e., the longest possible subsequence in which the elements of the subsequence are sorted in increasing order.

Examples:            

Input: arr[] = {3, 10, 2, 1, 20}
Output: 3
Explanation: The longest increasing subsequence is 3, 10, 20

Input: arr[] = {3, 2}
Output:1
Explanation: The longest increasing subsequences are {3} and {2}

Input: arr[] = {50, 3, 10, 7, 40, 80}
Output: 4
Explanation: The longest increasing subsequence is {3, 7, 40, 80} """

def solveLIS(vect):
    n = len(vect)
    memo = [[0 for _ in range(n+1)] for _ in range(n+1)]
    i = 0
    prec = -1 # valore precedente con cui è stato confrontato
    
    def LIS(i, prec):

        def is_greater(i, j):
            return j == n or vect[i] < vect[j] 

        if i == n:
            return 0
    
        if memo[i][prec] != 0:
            return memo[i][prec]
        
        memo[i][prec] = max((LIS(j, i) + int(is_greater(i,j))) for j in range (i+1, n+1))

        return memo[i][prec]
    
    return LIS(i, prec)

print(solveLIS([10, 9, 2, 5, 3, 7, 101, 18]))

# Time Complexity = O(n^2)