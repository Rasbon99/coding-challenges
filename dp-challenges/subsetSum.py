""" Given a set of non-negative integers and a value sum, the task is to check if there 
is a subset of the given set whose sum is equal to the given sum. 

Examples: 

Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output: True
Explanation: There is a subset (4, 5) with sum 9.

Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 30
Output: False
Explanation: There is no subset that add up to 30. """

def solveSubsetSum(set, sum):
    n = len(set)
    global memo
    memo = [[-1 for _ in range(sum+1)] for _ in range(n+1)]
    i = 0
    return bool(sumCheck(i, n, set, sum))
    
def sumCheck(i, n, set, sum):
    if sum == 0:
        memo[i][sum] = 1
        return memo[i][sum]
    
    if i == n or sum < 0:
        return 0
    
    if memo[i][sum] != -1:
        return memo[i][sum]
    
    memo[i][sum] = max(sumCheck(i+1, n, set, sum-set[i]), sumCheck(i+1, n, set, sum))

    return memo[i][sum]

print(solveSubsetSum([3, 34, 4, 12, 5, 2], 9))

print(solveSubsetSum([3, 34, 4, 12, 5, 2], 30))

# il programma funziona ma controlla tutte le possibilià di somma tra i sottoinsiemi 
# quando ne basterebbe una per far salire 1 e concludere

# Time Complexity O(n*sum)
