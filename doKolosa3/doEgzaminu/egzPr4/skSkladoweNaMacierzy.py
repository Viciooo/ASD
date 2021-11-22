def dfsProcessingTime(graph):
    V = len(graph)
    visited = [False]*V
    procTime = [-1]*V
    time = 1
    def dfs_visit(u):
        nonlocal graph,visited,procTime,time
        visited[u] = True
        for v in range(V):
            if graph[u][v] != 0 and not visited[v]:
                dfs_visit(v)
        procTime[u] = time
        time += 1

    for i in range(V):
        if visited[i] == False:
            dfs_visit(i)
    return procTime

def dfsSpSk(graph,s,visited):
    items = [s]

    def dfs_visit(u):
        nonlocal graph,visited,items
        visited[u] = True
        for v in range(len(graph)):
            if graph[u][v] != 0 and not visited[v]:
                dfs_visit(v)
                items.append(v)

    dfs_visit(s)
    return items

def revEdges(G,n):
    for i in range(n):
        for j in range(n):
            if G[i][j] == 1 and G[j][i] == 0:
                G[i][j] = 0
                G[j][i] = 2


def revEdgesBack(G,n):
    for i in range(n):
        for j in range(n):
            if G[i][j] == 2:
                G[i][j] = 0
                G[j][i] = 1

def findMaxVal(arr,visited):
    maxVal = -1
    maxi = None
    for i in range(len(arr)):
        if arr[i] > maxVal and visited[i] == False:
            maxi = i
            maxVal = arr[i]
    return maxi

def nadgorliwy_mag(G) -> list:
    #wydaje mi się że coś w stronę robimy krawędzie z każdego do każdego czyli odpalamy floyda i potem idziemy dfsem od początku spskł do końca
    n = len(G)
    solution = []
    visited = [False]*n
    procTime = dfsProcessingTime(G)
    curr = findMaxVal(procTime,visited)
    revEdges(G,n)
    while curr != None:
        solution.append(dfsSpSk(G,curr,visited))
        curr = findMaxVal(procTime,visited)
    revEdgesBack(G,n)
    return solution


G_1 = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]]

print(nadgorliwy_mag(G_1))

G_2 = [[0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0]]

print(nadgorliwy_mag(G_2))

G_3 = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]]

print(nadgorliwy_mag(G_3))






# niżej proszę nie patrzeć :))




odp_1 = 3
odp_2 = 2
odp_3 = 4