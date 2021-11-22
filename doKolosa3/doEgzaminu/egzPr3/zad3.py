#zł czasowa O(V*max_exp*Elog(V*max_exp))
#pamięciowa O(max_exp*n*n)

def fromMatrixToList(G):
    n = len(G)
    F = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if G[i][j] != 0:
                F[i].append([j,G[i][j]])
    return F

def isInPath(parent,i,exp,v):
    while i != None:
        if i == v:
            return True
        i,exp = parent[i][exp]
    return False

from queue import PriorityQueue
#można robić tablicę true false zamiast path ale to taka sama zł a mogę sb sprawdzić ścieżkę
def adventure(G, P, s, m, max_exp):
    Q = PriorityQueue()
    n = len(G)
    F = fromMatrixToList(G)
    d = [[float("inf") for _ in range(max_exp+1)] for _ in range(n)]
    visited = [[False for _ in range(max_exp+1)] for _ in range(n)]
    parent = [[(None,None) for _ in range(max_exp+1)] for _ in range(n)]
    d[m][0] = 0
    Q.put((0,m,0))
    while not Q.empty():
        _,u,exp = Q.get()
        if u == s:
            break
        if not visited[u][exp]:
            visited[u][exp] = True
            for v,w in F[u]:
                if v != 0 and not isInPath(parent,u,exp,v) and P[v][0] <= exp and d[v][min(exp+P[v][1],max_exp)] > d[u][exp] + w:
                    d[v][min(exp+P[v][1],max_exp)] = d[u][exp] + w
                    parent[v][min(exp+P[v][1],max_exp)] = (u,exp)
                    Q.put((d[v][min(exp+P[v][1],max_exp)],v,min(exp+P[v][1],max_exp)))
    odp = min(d[s])
    return odp if odp != float("inf") else None


G_1 = [
        [0, 0, 12, 5, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 7, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 0],
        [0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 3, 0, 2],
        [0, 4, 0, 0, 3, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10],
        [0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0],
        [0, 0, 0, 0, 10, 0, 100, 0, 0, 0, 0],
        ]
P_1 = [(None, None), (2, 7), (0, 7), (0, 2), (4, 6), (2, 5), (10, 2), (15, 1), (15, 2), (6, 8), (15, 100)]
m_1, s_1, max_exp_1 = 0, 10, 20
odp_1 = 27  # 0, 3, 5, 4, 6, 10

G_2 = [
        [0, 1, 15, 0, 0, 0, 0, 2],
        [0, 0, 2, 0, 0, 0, 0, 1],
        [0, 0, 0, 3, 5, 0, 0, 10],
        [0, 0, 0, 0, 4, 0, 0, 5],
        [0, 0, 0, 0, 0, 13, 10, 12],
        [0, 0, 0, 0, 0, 0, 9, 11],
        [1, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0],
        ]
P_2 = [(None, None), (0, 7), (0, 1), (2, 4), (10, 1), (10, 15), (3, 7), (20, 5)]
m_2, s_2, max_exp_2 = 0, 7, 20
odp_2 = 26  # 0, 1, 2, 3, 4, 6, 7


G_3 = [
        [0, 1, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
P_3 = [(None, None), (0, 1), (0, 2), (0, 5), (1, 4), (2, 4), (5, 3), (5, 1), (4, 5), (2, 6), (1, 7), (10, 2)]
m_3, s_3, max_exp_3 = 0, 11, 30
odp_3 = 9  # 0, 2, 5, 9, 11

G_4 = [[0,1,0,100,0],
        [0,0,1,0,0],
        [1,0,0,0,0],
        [0,0,0,0,100],
        [0,0,0,0,0]]
P_4 = [(None,None),(0,1),(0,1),(9,100),(102,1000)]
m_4,s_4,max_exp_4 = 0,4,103
odp_4 = None

print(adventure(G_4,P_4,s_4,m_4,max_exp_4))

G_5 = [[0,1,0,100,0],
        [0,0,1,0,0],
        [1,0,0,0,0],
        [0,0,0,0,100],
        [0,0,0,0,0]]
P_5 = [(None,None),(0,1),(0,1),(2,100),(102,1000)]
m_5,s_5,max_exp_5 = 0,4,103
odp_5 = 203
print(adventure(G_5,P_5,s_5,m_5,max_exp_5))

G_6 = [
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 100],
    [0, 0, 0, 0, 0],
    ]
P_6 = [(None, None), (0, 1), (0, 1), (0, 1), (3, 2)]
m_6, s_6, max_exp_6 = 0, 4, 10
odp_6 = 103  # 0, 1, 2, 3, 4
print(adventure(G_6,P_6,s_6,m_6,max_exp_6))

if __name__ == "__main__":
    tests = [[G_1, P_1, s_1, m_1, max_exp_1, odp_1], [G_2, P_2, s_2, m_2, max_exp_2, odp_2],
             [G_3, P_3, s_3, m_3, max_exp_3, odp_3]]

    problem = False

    for i in range(3):
        G_t, P_t, s_t, m_t, max_exp_t, odp = tests[i]
        if odp == adventure(G_t, P_t, s_t, m_t, max_exp_t):
            print("Test", i, "ok :)")
        else:
            print("Test", i, "źle :(")
            problem = True

    if not problem:
        print("Wszystko ok, dobra robota <3")