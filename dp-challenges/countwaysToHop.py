""" A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time. 
Implement a method to count how many possible ways the child can run up the stairs.

Examples: 

Input : 4
Output : 7
Explanation:
Below are the seven ways
 1 step + 1 step + 1 step + 1 step
 1 step + 2 step + 1 step
 2 step + 1 step + 1 step 
 1 step + 1 step + 2 step
 2 step + 2 step
 3 step + 1 step
 1 step + 3 step

Input : 3
Output : 4
Explanation:
Below are the four ways
 1 step + 1 step + 1 step
 1 step + 2 step
 2 step + 1 step
 3 step """

def solveCountWays(n):
    memo = [-1]*n
    i = 0

    def countWays(i):
        if i == n:
            return 1
        if i > n:
            return 0
        
        if memo[i] != -1:
            return memo[i]
        
        memo[i] = countWays(i+1) + countWays(i+2) + countWays(i+3)

        return memo[i]
    
    return countWays(i)

print(solveCountWays(4))

# Time Complexity = O(n)