from queue import Queue

def bfs(G,s):
    q = Queue()
    n = len(G)
    visited = [False]*n
    d = [float("inf")]*n

    q.put(s)
    d[s] = 0
    visited[s] = True

    while not q.empty():
        u = q.get()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                d[v] = d[u]+1
                q.put(v)

    return max(d)

def solve(arr,n):
    #na wejściu dostajemy listę ludzi którzy się znają bezpośrednio - ludzie są reprezentowani jako liczby od 0 do n-1
    #zakładam że dostajemy obie pary - coś muszę założyć a nie było sprecyzowane
    G = [[] for _ in range(n)]
    solution = [None for _ in range(n)]

    for i,j in arr:
        G[i].append(j)
        G[j].append(i)
    for i in range(n):
        solution[i] = bfs(G,i)
    return solution

arr = [(0,1),(1,4),(1,2),(2,3),(2,5),(4,5)]
print(solve(arr,6))
            
