#zł czasowa O(V^3 * logV) bo jestem ćwokiem i nie robię na macierzy
#zł pamięciowa O(V^2)

from zad3testy import runtests
from queue import PriorityQueue

def fromMatrixToList(G):
    n = len(G)
    F = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if G[i][j] != 0:
                F[i].append([j,G[i][j]])
    return F

def jumpGenerator(F,n):
    J = [[] for _ in range(n)]
    for i in range(n):
        for j,w1 in F[i]:
            for k,w2 in F[j]:
                if i != k:
                    J[i].append((k,max(w1,w2)))
    return J

def jumper(G, s, w):
    F = fromMatrixToList(G)
    n = len(G)
    J = jumpGenerator(F,n)
    Q = PriorityQueue()
    d = [[float("inf"),float("inf")] for _ in range(n)]
    visited = [[False,False] for _ in range(n)]
    #[bez butów,z butami]
    d[s][0] = 0
    Q.put((0,s,0))
    while not Q.empty():
        _,u,bootsUsed = Q.get()
        if u == w:
            break
        if not visited[u][bootsUsed]:
            visited[u][bootsUsed] = True
            for v,edge in F[u]:
                if d[v][0] > d[u][bootsUsed] + edge:
                    d[v][0] = d[u][bootsUsed] + edge
                    Q.put((d[v][0],v,0))
            if bootsUsed == 0:
                for v,edge in J[u]:
                    if d[v][1] > d[u][bootsUsed] + edge:
                        d[v][1] = d[u][bootsUsed] + edge
                        Q.put((d[v][1],v,1))
                
    return min(d[w])

runtests(jumper)