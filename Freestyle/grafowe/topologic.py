from queue import Queue

#zakładam że dostaję na wejściu adjList
def topologicSort(graph,s=0):
    visited = [False]*len(graph)
    q = Queue()
    def dfs_visit(u):
        nonlocal graph,visited,q
        visited[u] = True
        q.put(u)
        for v in graph[u]:
            if not visited[v]:
                dfs_visit(v)
    dfs_visit(s)
    while not q.empty():
        v = q.get()
        print(chr(ord(str(v))+49),end=' ')

adjList = [[1,2],[2,4],[],[],[3,5,6],[],[]]
topologicSort(adjList)