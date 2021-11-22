def bellmanFord(G,s):
    #używam reprezentacji listowej
    n = len(G)
    parent = [None for _ in range(n)]
    d = [float("inf") for _ in range(n)]
    d[s] = 0
    for _ in range(n-1):
        for j in range(n):
            for k in G[j]:
                if d[k[0]] > d[j] + k[1]:
                    d[k[0]] = d[j] + k[1]
                    parent[k[0]] = j
    #weryfikacja
    for j in range(n):
        for k in G[j]:
            if d[k[0]] > d[j] + k[1]:
                return False
    return d,parent

#zł O(VE)

G1 = [[(1,4),(3,5)] ,[(3,5)],[(1,-10)],[(2,3)]]
s1 = 0
# False
print(bellmanFord(G1,s1))  
G2 = [[(1, 6), (2, 5), (3, 5)], [(4, -1)], [(1, -2), (4, 1)], [(2, -2), (5, -1)], [(6, 3)], [(6, 3)], []]
s2 = 0
print(bellmanFord(G2,s2))   
# ([0, 1, 3, 5, 0, 4, 3], [None, 2, 3, 0, 1, 3, 4])
