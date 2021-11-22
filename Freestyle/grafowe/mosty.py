#zakładam że graf spójny - przynajmniej na razie
def dfsVisitTime(G):
    n = len(G)
    visited = [False]*n
    time = 1
    d = [None]*n
    low = [None]*n

    def dfsVisit(u):
        nonlocal G,visited,time,d,low
        visited[u] = True
        d[u] = time
        low[u] = time
        for v in G[u]:
            if not visited[v]:
                time += 1
                dfsVisit(v)
                low[u] = min(low[u],low[v])
            elif visited[v] and d[v]+1 != d[u]:
                low[u] = min(low[u],d[v])

    dfsVisit(0)
    for i in range(1,n):
        if low[i] == d[i]:
            for j in range(n):
                if d[j] == d[i]-1:
                    print("edge ",i," ",j)
                    break

G = [[1,6],[0,2],[1,3,6],[2,4,5],[3,5],[3,4],[0,2,7],[6]]
dfsVisitTime(G)

#gówno tam a nie niedziała