""" Given an array arr[] where each element represents the max number of steps that can be made forward from that index. 
The task is to find the minimum number of jumps to reach the end of the array starting from index 0.

Examples: 

Input: arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9}
Output: 3 (1-> 3 -> 9 -> 9)
Explanation: Jump from 1st element to 2nd element as there is only 1 step.
Now there are three options 5, 8 or 9. If 8 or 9 is chosen then the end node 9 can be reached. So 3 jumps are made.

Input:  arr[] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1}
Output: 10
Explanation: In every step a jump is needed so the count of jumps is 10. """

def solveJumpGame(arr):
    n = len(arr)
    memo = [[-1 for _ in range(n+1)] for _ in range(n+1)]
    i, j = 0, -1

    def jump(i, j):
        if i >= n:
            return 0
        if j >= n:
            return float('inf')
        
        if memo[i][j] != -1:
            return memo[i][j]
        
        memo[i][j] = max(jump(i + k + 1, i) + 1 for k in range(arr[i]))

        return memo[i][j]
    
    return jump(i, j)

print(solveJumpGame([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]))

# Time complexity = O(n^2)