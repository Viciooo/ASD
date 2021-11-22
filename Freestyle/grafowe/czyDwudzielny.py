
adjList = [[1,2,5],[2],[1,0],[],[5],[4,0]]
arr= [[5,4,3],[5,4,3],[5,4,3],[0,1,2],[0,1,2],[0,1,2]]
G3 = [[], [3, 4, 5], [3, 4, 5], [1, 2], [1, 2], [1, 2]]

def dfsModified(G):
    n = len(G)
    visited = [None]*n

    def dfs_visit(u,val):
        nonlocal G,visited
        visited[u] = val
        for v in G[u]:
            if visited[v] == None:
                dfs_visit(v,not val)
            elif visited[v] == val:
                return False
        return True
    
    for i in range(n):
        if visited[i] == None:
            if dfs_visit(i,True) == False:
                return False
    return True
print(dfsModified(G3))
print(dfsModified(arr))
print(dfsModified(adjList))
#puścić dfs i kolorowac
#ctrl h to jest fajna sprawa 