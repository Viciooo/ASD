from queue import Queue
# Mamy mapę miasteczka, w którym są domy i sklepy. Na mapie są również drogi (każda długości 1), 
# które łączą dom z domem, albo dom ze sklepem. 
# Naszym zadaniem jest, dla każdego domu, znaleźć odległość do najbliższego sklepu.
def solve(G,S):
    q = Queue()
    n = len(G)
    m = len(S)
    visited = [False]*n
    d = [-1]*n
    for i in range(m):
        q.put(S[i])
        d[S[i]] = 0
        visited[S[i]] = True
    while not q.empty():
        u = q.get()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                d[v] = d[u]+1
                q.put(v)
    return d

G = [[1],[0,2,4],[3,1],[2,5,4],[1,3,5],[3,4]]
S = [1,3]
print(solve(G,S))