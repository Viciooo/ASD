def d(x1,y1,x2,y2):
    return ((x1-x2)**2 + (y1-y2)**2)**(0.5)

#jak chcemy oszczędzać pamięć to nie budujemy grafu tylko iterujemy po odległościach licząc je na bieżąco

from queue import Queue
def zabaMonika(arr,L):
    n = len(arr)
    G = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            G[i][j] = d(arr[i][0],arr[i][1],arr[j][0],arr[j][1])
    Q = Queue()
    visited = [[False,False] for _ in range(n)]
    dist = [[float("inf"),float("inf")] for _ in range(n)]
    Q.put((0,0))
    #(wierzchołek,czym dotarłem(0 - normalnie,1 - duzy skok))
    visited[0][0] = True
    dist[0][0] = 0
    while not Q.empty():
        u,typeOfJump = Q.get()
        if u == n-1:
            break
        for v in range(n):
            if G[u][v] > 0.5*L and typeOfJump == 1:
                continue
            if typeOfJump == 1 and G[u][v] <= 0.5*L and not visited[v][0]:
                visited[v][0] = True
                Q.put((v,0))
                dist[v][0] = dist[u][1]+1
            if typeOfJump == 0 and G[u][v] <= L and not visited[v][0]:
                visited[v][0] = True
                Q.put((v,0))
                dist[v][0] = dist[u][0]+1
            if typeOfJump == 0 and G[u][v] <= 2*L and not visited[v][1]:
                visited[v][1] = True
                Q.put((v,1))
                dist[v][1] = dist[u][0]+1

    result = min(dist[n-1])

    return None if result == float("inf") else result

T1 = [(2, 2), (3, 5), (5, 6), (6, 10), (11, 7)]
odp1 = 3
print(zabaMonika(T1, 4.1))

T2 = [(2, 2), (3, 5), (5, 6), (6, 10), (11, 7)]
odp2 = 2
print(zabaMonika(T2, 5))

T3 = [(2, 2), (3, 5), (5, 6), (6, 10), (11, 7)]
odp3 = 1
print(zabaMonika(T3, 5.2))

T4 = [(2, 2), (3, 5), (5, 6), (6, 10), (11, 7)]
odp4 = 1
print(zabaMonika(T4, 1))