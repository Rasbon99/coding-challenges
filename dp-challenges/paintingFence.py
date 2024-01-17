""" Given a fence with n posts and k colors, find out the number of ways of painting the fence 
such that at most 2 adjacent posts have the same color. Since the answer can be large return it modulo 10^9 + 7.

Examples:

Input : n = 2 k = 4
Output : 16
Explanation: We have 4 colors and 2 posts.
Ways when both posts have same color : 4 
Ways when both posts have diff color :4(choices for 1st post) * 3(choices for 2nd post) = 12

Input : n = 3 k = 2
Output : 6 """

def solvePaintingFence(n, k):
    mod = 10**9 + 7
    memo = [[-1 for _ in range(3)] for _ in range(n+1)]

    def paint(i, same):
        if i == n:
            return 1
        if memo[i][same] != -1:
            return memo[i][same]
        
        res = 0
        # Se l'ultimo palo ha lo stesso colore del palo precedente
        if same:
            res = (paint(i+1, 0) * (k-1)) % mod
        else:
            # Se l'ultimo palo ha un colore diverso dal palo precedente
            res = ((paint(i+1, 0) * (k-1)) % mod + (paint(i+1, 1) * 1) % mod) % mod
        
        memo[i][same] = res
        return res

    return (paint(1, 0) * k) % mod

print(solvePaintingFence(2,4))

# Time Complexity = o(n)

# Non fatto da me