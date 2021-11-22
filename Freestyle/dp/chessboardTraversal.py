def tabDpSol(cost,n):
    grid = [[None for _ in range(n)] for _ in range(n)]
    grid[0][0] = cost[0][0]
    for i in range(1,n):
        grid[i][0] = grid[i-1][0] + cost[i][0]
        grid[0][i] = grid[0][i-1] + cost[0][i]
    for r in range(1,n):
        for c in range(1,n):
            grid[r][c] = min(grid[r-1][c],grid[r][c-1]) + cost[r][c]
    return grid[n-1][n-1]

arr = [[1,2,3],[4,5,6],[7,8,9]]
print(tabDpSol(arr,3))