# Dany jest graf nieskierowany G = (V,E) z ważonymi krawędziami (w: E -> N). 
# Proszę zaproponować jak najszybszy algorytm, który znajduje ścieżkę
# z danego wierzchołka s do danego wierzchołka t taką, że:
# 1.Każda kolejne krawędź ma mniejszą wagę niż poprzednia
# 2.Spośród ścieżek spełniających powyższy warunek, znaleziona ma najmniejszą sumę wag


from queue import PriorityQueue
def descendingPath(G,s,t):
    n = len(G)
    idx = [0 for _ in range(n)]
    parent = [[] for _ in range(n)]
    for i in range(n):
        G[i].sort(key=lambda x: x[1])
    q = PriorityQueue()
    q.put([0,float("inf"),s])
    while not q.empty():
        d,last,u = q.get()
        if u == t:
            break
        while idx[u] < len(G[u]) and G[u][idx[u]][1] < last:
            q.put([d+G[u][idx[u]][1],G[u][idx[u]][1],G[u][idx[u]][0]])
            parent[G[u][idx[u]][0]].append([d+G[u][idx[u]][1],u,G[u][idx[u]][1]])
            idx[u] += 1
    for i in range(n):
        parent[i].sort(key=lambda x: x[0])
    path = [t]
    last = -float("inf")
    u = t
    while u != s:
        tmp = u
        for i in range(len(parent[u])):
            if parent[u][i][2] > last:
                last = parent[u][i][2]
                u = parent[u][i][1]
                path.append(u)
                break
        if u == tmp:
            return "There is no such way"
    path.reverse()
    return path

G1 = [
    [[2, 100], [1, 4]],  # 0
    [[0, 4], [4, 3]],   # 1
    [[3, 200], [0, 100], [4, 4]],   # 2
    [[2, 200], [4, 3]],  # 3
    [[2, 4], [1, 3], [3, 3]]  # 4
]
print(descendingPath(G1, 0, 3))
# print(descendingPath(G1, 2, 3))
# print(descendingPath(G1, 4, 0))