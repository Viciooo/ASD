from collections import deque

G = [[0,1,1,0,0,0],
    [1,0,1,1,0,1],
    [1,1,0,0,1,1],
    [0,1,0,0,0,1],
    [0,0,1,0,0,1],
    [0,1,1,1,1,0]]

def euler(G):
    n = len(G)
    m_cnt = 0
    for r in range(n):
        cnt = 0
        for c in range(n):
            if G[r][c] == 1:
                cnt += 1
        if cnt % 2 == 1:
            return
        m_cnt += cnt
    solution = [0]*(m_cnt//2 + 1)
    cycle = deque()
    dfs_visit(0,G,cycle,n)
    for i in range(m_cnt//2 + 1):
        solution[i] = cycle.popleft()
    return solution

def dfs_visit(s,graph,cycle,n,bannedEdges=[]): 
    for v in range(n):
        if v not in bannedEdges and graph[s][v] == 1:
            dfs_visit(v,graph,cycle,n,bannedEdges+[s])
    cycle.appendleft(s)

print(euler(G))