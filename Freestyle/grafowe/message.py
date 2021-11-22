from queue import Queue
def solve(graph,n):
    visited = [False]*n
    d = [-1]*n
    d[0] = 0
    q = Queue()
    q.put(0)
    visited[0] = True
    while not q.empty():
        u = q.get()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                d[v] = d[u] + 1
                q.put(v)
    #lecimy countingiem bo mamy ograniczenie od góry na ilość fal(nie ma fal nie ma fal...) przez ilość wierzchołków
    fale = [0]*n
    for v in d:
        fale[v] += 1
    return max(fale)

# adjList = [[1,4],[0,2],[1],[4],[0,3]]
def message(graph,n):
    adjList = [[] for _ in range(n)] #potensial błąd
    for i in range(len(graph)):
        adjList[graph[i][0]].append(graph[i][1])
        adjList[graph[i][1]].append(graph[i][0])
    return solve(adjList,n)

graph = [(0,1),(0,4),(1,0),(1,2),(2,1),(3,4),(4,0),(4,3)]
print(message(graph,5))