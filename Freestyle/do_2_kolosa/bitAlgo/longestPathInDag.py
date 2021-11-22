'''
f(i) - najdłuższa ścieżka kończąca się w wierzchołku i
f(i) = max(f(j)+1), j to dzieci i
'''

def solve(G):
    n = len(G)
    F = [0 for _ in range(n)]
    visited = [False for _ in range(n)]
    def dfsVisit(u):
        nonlocal G,visited,F
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                dfsVisit(v)
            F[u] = max(F[u],F[v]+1)
    for i in range(n):
        if not visited[i]:
            dfsVisit(i)
    return max(F)

G = [[1],[],[1,4,5],[2],[],[6,7,8],[],[],[]]
print(solve(G))