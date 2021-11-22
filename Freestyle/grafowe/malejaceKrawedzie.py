# Zadanie 6. (malejace krawedzie) (implementacja) Dany jest graf G = (V,E), gdzie kazda krawedz
# ma wage ze zbioru {1, . . . , |E|} (wagi krawedzi sa parami rózne). Prosze zaproponowac algorytm, który dla
# danych wierzchołków x i y sprawdza, czy istnieje sciezka z x do y, w której przechodzimy po krawedziach o
# coraz mniejszych wagach.
G = [[1,2],[3],[3],[4,5],[5],[6],[]]
W = [[11,16],[10],[15],[12,13],[10],[11],[]]
def check(G,W,x,y):
    n = len(G)
    visited = [False]*n
    flag = False

    def dfsVisit(u,w=float("inf")):
        nonlocal G,visited,y,flag
        visited[u] = True
        if u == y:
            flag = True
            return True
        for i in range(len(G[u])):
            if not visited[G[u][i]] and W[u][i]<w:
                dfsVisit(G[u][i],W[u][i])
                # visited[G[u][i]] = true
    dfsVisit(x)
    return flag

print(check(G,W,0,6))
