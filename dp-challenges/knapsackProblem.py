""" Given N items where each item has some weight and profit associated with it and also given a bag with capacity W, 
[i.e., the bag can hold at most W weight in it]. The task is to put the items into the bag such that the sum of profits 
associated with them is the maximum possible. 

Note: The constraint here is we can either put an item completely into the bag or cannot put it at all 
[It is not possible to put a part of an item into the bag].

Input: N = 3, W = 4, profit[] = {1, 2, 3}, weight[] = {4, 5, 1}
Output: 3
Explanation: There are two items which have weight less than or equal to 4. 
If we select the item with weight 4, the possible profit is 1. And if we select the item with weight 1, 
the possible profit is 3. So the maximum possible profit is 3. Note that we cannot put both the items with weight 4 and 1 
together as the capacity of the bag is 4.

Input: N = 3, W = 3, profit[] = {1, 2, 3}, weight[] = {4, 5, 6}
Output: 0 """

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
            take = knp(i+1, x+weight[i]) + profit[i]
        
        not_take = knp(i+1, x)

        
        memo[i][x] = max(take, not_take)

        return memo[i][x]
    
    return knp(i, x)

print(solveKnapsack([60, 100, 120], [10, 20, 30], 50))