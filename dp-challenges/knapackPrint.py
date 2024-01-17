""" Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value 
in the knapsack. In other words, given two integer arrays, val[0..n-1] and wt[0..n-1] represent values and weights 
associated with n items respectively. Also given an integer W which represents knapsack capacity, find out the items 
such that sum of the weights of those items of a given subset is smaller than or equal to W. You cannot break an item, 
either pick the complete item or don’t pick it (0-1 property).

Input : val[] = {60, 100, 120};
        wt[] = {10, 20, 30};
        W = 50;
Output : 220 //maximum value that can be obtained
         30 20 //weights 20 and 30 are included. 

Input : val[] = {40, 100, 50, 60};
        wt[] = {20, 10, 40, 30};
        W = 60;
Output : 200
         30 20 10 """

def solveKnapsack(profit, weight, W):
    n = len(profit)
    memo = [[-1 for _ in range(W+1)] for _ in range(n+1)]
    i, x = 0, 0
    res = []

    def knp(i, x):

        if i == n:
            return 0
        
        if memo[i][x] != -1:
            return memo[i][x]
        
        take, not_take = 0, 0

        if x + weight[i] <= W:
            take = knp(i+1, x+weight[i]) + profit[i]
            res.append(weight[i])

        
        not_take = knp(i+1, x)

        
        memo[i][x] = max(take, not_take)

        if memo[i][x] == not_take and x + weight[i] <= W:
            res.remove(weight[i])

        return memo[i][x]
    
    return knp(i, x), res

print(solveKnapsack([60, 100, 120], [10, 20, 30], 50)) # non so ma non va