from queue import PriorityQueue

def getSolution(parent,s,t,fuel):
    if t == s:
        return [(s,fuel)]
    return getSolution(parent,s,parent[t][fuel][0],parent[t][fuel][1]) + [(t,fuel)]

def solve(G,P,D,s,t):
    #G to lista adjacencji a P to ceny paliwa w wierzchołkach, D to pojemność baku
    n = len(P)
    visited = [[False for _ in range(D+1)] for _ in range(n)]
    d = [[float("inf") for _ in range(D+1)] for _ in range(n)]
    parent = [[None for _ in range(D+1)] for _ in range(n)]
    Q = PriorityQueue()
    for i in range(D+1):
        d[s][i] = i*P[s]
        Q.put((d[s][i],s,i))
        #(koszt,dokąd,z jaką ilością paliwa)
    while not Q.empty():
        _,u,f = Q.get()
        if u == t:
            break
        if not visited[u][f]:
            visited[u][f] = True
            for v,w in G[u]:
                currFuel = f - w
                if currFuel >= 0:
                    for i in range((D-currFuel)+1):
                        tankPrice = i * P[v]
                        if d[v][currFuel+i] > tankPrice + d[u][f]:
                            d[v][currFuel+i] = tankPrice + d[u][f]
                            Q.put((d[v][currFuel+i],v,currFuel+i))
                            parent[v][currFuel+i] = [u,f]
    path = getSolution(parent,s,t,0)
    print(path)
    return min(d[t])

G = [
    [[1, 7], [6, 3]],  # 0
    [[0, 7], [2, 3], [7, 4]],  # 1
    [[1, 3], [3, 8], [7, 4]],  # 2
    [[2, 8], [4, 3], [5, 10]],  # 3
    [[3, 3], [5, 8]],  # 4
    [[3, 10], [4, 8], [6, 6], [7, 3]],  # 5
    [[0, 3], [5, 6], [7, 5]],  # 6
    [[1, 4], [2, 4], [5, 3], [6, 5]]  # 7
]


S = [8, 5, 9, 700, 3, 3, 2, 1]  # gas stations
D = 10
a = 0
b = 4 
print(solve(G,S,D,a,b))

# G1 = [[(1,1),(2,1)],[(0,1),(2,2)],[(0,1),(1,2),(3,3)],[(2,3),(4,95)],[(3,95)]]
# D1 = 100
# S1 = [1,2,3,4,1]
# a1 = 0
# b1 = 4
# print(solve(G1,S1,D1,a1,b1))