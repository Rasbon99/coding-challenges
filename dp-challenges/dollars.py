""" New Zealand currency consists of $100, $50, $20, $10, and $5 notes and $2, $1, 50c, 20c, 10c and 5c
coins. Write a program that will determine, for any given amount, in how many ways that amount
may be made up. Changing the order of listing does not increase the count. Thus 20c may be made
up in 4 ways: 1×20c, 2×10c, 10c+2×5c, and 4×5c.
Input
Input will consist of a series of real numbers no greater than $300.00 each on a separate line. Each
amount will be valid, that is will be a multiple of 5c. The file will be terminated by a line containing
zero (0.00).
Output
Output will consist of a line for each of the amounts in the input, each line consisting of the amount
of money (with two decimal places and right justified in a field of width 6), followed by the number of
ways in which that amount may be made up, right justified in a field of width 17.
Sample Input
0.20
2.00
0.00
Sample Output
0.20 4
2.00 293 """


def solveDollars(amount):
    dollars = [100.0, 50.0, 20.0, 10.0, 5.0, 2.0, 1.0, 0.50, 0.20, 0.10, 0.05]
    n = len(dollars)
    amount = int(amount * 100)
    memo = [[0 for _ in range(amount+1)] for _ in range(n+1)]
    i = 0
    sum = 0

    def dp(i, sum):
        if i == n:
            return 0
        if sum > amount:
            return 0
        if sum == amount:
            return 1
        
        if memo[i][sum] != 0:
            return memo[i][sum]
        
        if sum <= amount:
            memo[i][sum] += dp(i, sum+int(dollars[i]*100))  # use the current coin
            memo[i][sum] += dp(i+1, sum)  # skip the current coin

        return memo[i][sum]
    
    return dp(i, sum)

print(solveDollars(1.0))




    