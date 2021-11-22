def getDiamiterOfG(G):
    n = len(G)
    visited = [False]*n
    def dfsVisit(u,time):
        nonlocal G,visited
        visited[u] = time
        for v in G[u]:
            if visited[v] == False:
                dfsVisit(v,time+1)
    dfsVisit(0,1)
    x = 0
    for i in range(1,n):
        if visited[i] > visited[x]:
            x = i
    visited = [False]*n
    dfsVisit(x,1)
    y = 0
    for i in range(1,n):
        if visited[i] > visited[y]:
            y = i
    return max(visited)

G = [[1,2],[3,4,0],[0],[1],[1]]
print(getDiamiterOfG(G))
