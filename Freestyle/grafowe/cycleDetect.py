def cycleDetect(graph):
    v = len(graph)
    visited = [False]*v
    parent = [None]*v

    def dfs_visit(i):
        nonlocal graph,visited,parent
        visited[i] = True
        for u in graph[i]:
            if visited[u] == False:
                parent[u] = i
                dfs_visit(u)
            elif u == parent[i]:
                continue
            else:
                return True
        return False

    sol = False
    for i in range(v):
        if not visited[i]:
            sol = sol or dfs_visit(i)
    return sol


arr0 = [[1,4],[0,4,3,2],[1,3],[1,2,4],[0,3,1]] #True
arr1 = [[1,4],[0,2],[1],[4],[0,3]] #False
arr2 = [[1,2,5],[2],[1,0],[],[5],[4,0]] #True
arr3 = [[],[2,3],[1,3],[1,2]] #True
print(cycleDetect(arr1))