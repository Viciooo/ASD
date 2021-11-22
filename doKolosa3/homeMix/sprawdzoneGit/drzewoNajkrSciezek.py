# Dany jest graf ważony  G, oraz drzewo rozpinające T zawierające wierzchołek s. 
# Podaj algorytm, który sprawdzi, czy T jest drzewem najkrótszych ścieżek od wierzchołka s.

def dfsButWeighted(G,s,n):
    visited = [False]*n
    d = [float("inf") for _ in range(n)]
    d[s[1]] = 0
    def dfsVisit(u):
        nonlocal G,visited
        visited[u[1]] = True
        for v in G[u[1]]:
            if not visited[v[1]]:
                d[v[1]] = d[u[1]] + v[0]
                dfsVisit(v)
    dfsVisit(s)
    return d

def solve(G,T):
    n = len(G)
    d = dfsButWeighted(T,(0,0),n)
    for i in range(n):
        for j in G[i]:
            if d[i] + j[0] < d[j[1]]:
                return False
    return True

G1 = [[(1,6),(float("inf"),1)],[(float("inf"),0),(1,2),(3,3),(7,6),(3,5),(11,4)],[(1,1),(5,3)],[(5,2),(3,1)],[(11,1),(3,5)],[(3,4),(2,6),(3,1)],[(2,5),(7,1),(1,0)]]
T1 = [[(1,6)],[(1,2),(3,3),(3,5)],[(1,1)],[(3,1)],[(3,5)],[(3,4),(2,6),(3,1)],[(2,5),(1,0)]]
print(solve(G1,T1))#True

G2 = [[(1,6),(3,1)],[(3,0),(1,2),(3,3),(7,6),(3,5),(11,4)],[(1,1),(5,3)],[(5,2),(3,1)],[(11,1),(3,5)],[(3,4),(2,6),(3,1)],[(2,5),(7,1),(1,0)]]
T2 = [[(1,6)],[(1,2),(3,3),(3,5)],[(1,1)],[(3,1)],[(3,5)],[(3,4),(2,6),(3,1)],[(2,5),(1,0)]]
print(solve(G2,T2))#False