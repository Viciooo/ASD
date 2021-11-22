#implementacja grafu w postaci listy sąsiedztwa

#np:
adjList = [[1,2,5],[2],[1,0],[],[5],[4,0]]

def dfs(G,s):
    visited = [False]*len(G)

    def dfsVisit(u):
        nonlocal G,visited
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                dfsVisit(v)

    dfsVisit(s)

#narażone na plagiat (!)