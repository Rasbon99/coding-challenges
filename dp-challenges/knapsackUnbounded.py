""" Given a knapsack weight W and a set of n items with certain value vali and weight wti, we need to calculate the maximum 
amount that could make up this quantity exactly. This is different from classical Knapsack problem, here we are allowed 
to use unlimited number of instances of an item.

Note: N is always positive i.e greater than zero

Input : W = 100
       val[]  = {1, 30}
       wt[] = {1, 50}
Output : 100
There are many ways to fill knapsack.
1) 2 instances of 50 unit weight item.
2) 100 instances of 1 unit weight item.
3) 1 instance of 50 unit weight item and 50
   instances of 1 unit weight items.
We get maximum value with option 2.

Input : W = 8
       val[] = {10, 40, 50, 70}
       wt[]  = {1, 3, 4, 5}       
Output : 110 
We get maximum value with one unit of
weight 5 and one unit of weight 3. """

def solveKnapsack(profit, weight, W):
    n = len(profit)
    memo = [[-1 for _ in range(W+1)] for _ in range(n+1)]
    i, x = 0, 0

    def knp(i, x):
        if i == n:
            return 0
        
        if memo[i][x] != -1:
            return memo[i][x]
        
        take, not_take = 0, 0

        if x + weight[i] <= W:
            take = knp(i, x+weight[i]) + profit[i]
        
        not_take = knp(i+1, x)

        
        memo[i][x] = max(take, not_take)

        return memo[i][x]
    
    return knp(i, x)

print(solveKnapsack([1, 30], [1, 50], 100))