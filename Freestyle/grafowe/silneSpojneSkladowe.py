#Reprezentacja jako lista adjencji
def dfsProcessingTime(graph):
    V = len(graph)
    visited = [False]*V
    procTime = [-1]*V
    time = 1
    def dfs_visit(u):
        nonlocal graph,visited,procTime,time
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
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
        for v in graph[u]:
            if not visited[v]:
                items.append(v)
                dfs_visit(v)

    dfs_visit(s)
    return items

def revEdges(G,n):
    new = [[] for _ in range(n)]
    for i in range(n):
        for j in G[i]:
            new[j].append(i)
    return new

def findMaxVal(arr,visited):
    maxVal = -1
    maxi = None
    for i in range(len(arr)):
        if arr[i] > maxVal and visited[i] == False:
            maxi = i
            maxVal = arr[i]
    return maxi

def silSpSk(G):
    n = len(G)
    solution = []
    visited = [False]*n
    procTime = dfsProcessingTime(G)
    curr = findMaxVal(procTime,visited)#TODO
    new = revEdges(G,n)
    print(procTime)
    while curr != None:
        print(curr)
        solution.append(dfsSpSk(new,curr,visited))
        # print(visited)
        curr = findMaxVal(procTime,visited)
    return solution

G = [[2,4],[0,9],[1],[4,6],[5],[3],[5],[9,3],[7],[10],[8,6]]
print(silSpSk(G))
#problem z items