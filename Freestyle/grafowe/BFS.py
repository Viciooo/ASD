from queue import Queue

def bfs(G,s):
    q = Queue()
    n = len(G)
    visited = [False]*n
    d = [-1]*n

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

#narażone na plagiat (!)


def matrixBfs(graph,s=0):
    q = Queue()
    n = len(graph)
    visited = [False]*n
    d = [-1]*n
    q.put(s)
    visited[s] = True
    while not q.empty():
        u = q.get()
        for v in range(n):
            if graph[u][v] == 1:
                if not visited[v]:
                    visited[v] = True
                    q.put(v)
                    d[v] = d[u]+1


# adjList = [[1,2],[2,4],[],[],[3,5,6],[],[]]
# arr =   [[0,1,1,0,0,0,0]
#         ,[0,0,1,0,1,0,0]
#         ,[0,0,0,0,0,0,0]
#         ,[0,0,0,0,0,0,0]
#         ,[0,0,0,1,0,1,1]
#         ,[0,0,0,0,0,0,0]
#         ,[0,0,0,0,0,0,0]]   
# matrixBfs(arr)