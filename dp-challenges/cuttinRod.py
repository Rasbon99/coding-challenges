""" Given a rod of length n inches and an array of prices that includes prices of all pieces of 
size smaller than n. Determine the maximum value obtainable by cutting up the rod and selling the pieces. 
For example, if the length of the rod is 8 and the values of different pieces are given as the following, 
then the maximum obtainable value is 22 (by cutting in two pieces of lengths 2 and 6) 

length   | 1   2   3   4   5   6   7   8  
--------------------------------------------
price    | 1   5   8   9  10  17  17  20
And if the prices are as follows, then the maximum obtainable value is 24 (by cutting in eight pieces of length 1) 

length   | 1   2   3   4   5   6   7   8  
--------------------------------------------
price    | 3   5   8   9  10  17  17  20 """

def solveCuttinRod(rod):
    n = len(rod)
    global memo
    memo = [[-1 for _ in range(n+1)] for _ in range(n+1)]
    i = 0
    x = n

    def maxGain(i, x):
        if i == n+1 or x == 0:
            return 0
        
        if memo[i][x] != -1:
            return memo[i][x]
        
        if i+1 <= x:
            memo[i][x] = max(maxGain(i, x-(i+1)) + rod[i], maxGain(i+1, x))
        else:
            memo[i][x] = maxGain(i+1, x)

        return memo[i][x]
    
    return maxGain(i, x)

print(solveCuttinRod([1, 5, 8, 9, 10, 17, 17, 20]))

print(solveCuttinRod([3, 5, 8, 9, 10, 17, 17, 20]))

# Time Complexity O(n*n)