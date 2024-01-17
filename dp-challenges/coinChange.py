""" Given an integer array of coins[ ] of size N representing different types of denominations and an 
integer sum, the task is to count the number of coins required to make a given value sum.  

Note: Assume that you have an infinite supply of each type of coin. 

Examples: 

Input: sum = 4, coins[] = {1,2,3}, 
Output: 4
Explanation: there are four solutions: {1, 1, 1, 1}, {1, 1, 2}, {2, 2}, {1, 3}.  """

def solveCoinChange(coin, sum):
    n = len(coin)
    global memo
    memo = [[-1 for _ in range(sum+1)] for _ in range(n+1)]
    i = 0
    return sumCounter(i, coin, n, sum)             # il dp è il counter stesso, passo sum di modo da decrementarla e non avere 

def sumCounter(i, coin, n, sum):
    if sum == 0:
        memo[i][sum] = 1
        return memo[i][sum]
    
    if i == n or sum < 0:
        return 0
    
    if memo[i][sum] != -1:
        return memo[i][sum]
    
    memo[i][sum] = sumCounter(i+1, coin, n, sum) + sumCounter(i, coin, n, sum-coin[i])

    return memo[i][sum]


print(solveCoinChange([2,5,3,6], 10))

# Time Complexity = O(n*sum)
             