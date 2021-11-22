from queue import PriorityQueue

def getSolution(parent,a,i,who):
    if parent[i][who] == None:
        return [a]
    return getSolution(parent,a,parent[i][who],(who+1)%2) + [i]

def djikstraAliceBob(G,a,b):
    Q = PriorityQueue()
    n = len(G)
    parent = [[None for _ in range(2)] for _ in range(n)]
    d = [[float("inf") for _ in range(2)] for _ in range(n)]
    visited = [[False for _ in range(2)] for _ in range(n)]
    d[a][0] = 0
    d[a][1] = 0
    Q.put((0,a,1))
    Q.put((0,a,0))
    while not Q.empty():
        _,u,who = Q.get()
        if u == b:
            break
        if not visited[u][who]:
            visited[u][who] = True
            for v in range(n):
                w = G[u][v]
                if w != 0:
                    if who == 1:
                        if d[v][0] > d[u][1]:
                            d[v][0] = d[u][1]
                            parent[v][0] = u
                    else:
                        if d[v][1] > d[u][0] + w:
                            d[v][1] = d[u][0] + w
                            parent[v][1] = u
                    Q.put((d[v][(who+1)%2],v,(who+1)%2))

    if d[b] == [float("inf"),float("inf")]:
        return (None,None,None)
    if d[b][0] < d[b][1]:
        imie = "Bob"
        dist = d[b][0]
        solution = getSolution(parent,a,b,0)
    else:
        imie = "Alicja"
        dist = d[b][1]
        solution = getSolution(parent,a,b,1)
    return (imie,dist,solution)

G1= [[0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 120],
    [0, 0, 0, 0, 0, 0, 0, 0]]
a1,b1 = 0,7
odp1 = ("Bob",6,[0,1,2,3,4,5,6,7])

G2 = [[0, 1, 0, 0, 0, 15, 0, 0], [0, 0, 5, 0, 0, 0, 0, 0], [0, 0, 0, 0, 7, 0, 110, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 7, 0, 0, 8, 100, 90], [0, 0, 0, 0, 8, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 7, 0]]
a2,b2 = 0,6
odp2 = ("Bob",5,[0,1,2,6])

G3 = [[0, 100, 50], [0, 0, 12], [0, 0, 0]]
a3,b3 = 0,2
odp3 = ("Bob",0,[0,2])

G4 = [[0, 100, 50, 0, 0], [0, 0, 12, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
a4,b4 = 0,4
odp4 = (None,None,None)

G5= [[0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0]]
a5,b5 = 0,7
odp5 = ("Alicja",4,[0,1,2,3,4,5,6,7])
# print(djikstraAliceBob(G5,a5,b5))