def solveUnidirectionalTSP(n, m, matrix):
    memo = [[-1 for _ in range(m+1)] for _ in range(n+1)]
    path = [[-1 for _ in range(m+1)] for _ in range(n+1)]

    def uTSP(i, j):
        if j == m:
            return 0

        if i == n:
            i = 0
        if i == -1:
            i = n-1

        if memo[i][j] != -1:
            return memo[i][j]
        
        choices = [uTSP(i-1, j+1) + matrix[i][j],
                   uTSP(i, j+1) + matrix[i][j],
                   uTSP(i+1,j+1) + matrix[i][j]]
        
        memo[i][j] = min(choices)
        path[i][j] = choices.index(memo[i][j]) - 1
        
        return memo[i][j]
    
    min_list = []
    for i in range(n):
        min_list.append(uTSP(i, 0))
    
    min_path = []
    min_index = min_list.index(min(min_list))
    for j in range(m):
        min_path.append(min_index + 1)
        min_index = (min_index + path[min_index][j])
    
    return min(min_list), min_path

dims = input("inserire rows e cols: ")

n, m = map(int, dims.strip().split(" "))

matrix = []
for i in range(n):
    linea = input("inserire riga " + str(i+1) + ":")

    matrix.append(list(map(int, linea.strip().split(" "))))

print(solveUnidirectionalTSP(n, m, matrix))