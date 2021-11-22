# Zadanie 4. (sklejanie odcinków) Dany jest ciag przedziałów postaci [ai, bi]. Dwa przedziały mozna
# skleic jesli maja dokładnie jeden punkt wspólny. Prosze wskazac algorytmy dla nastepujacych problemów:
# 1. Problem stwierdzenia, czy da sie uzyskac przedział [a, b] przez sklejanie odcinków.
# 2. Problem stwierdzenia jaki najdłuzszy odcinek mozna uzyskac sklejajac najwyzej k odcinków.

#1
from queue import Queue

def przerabiamy(edge_arr, target):
    adj_list = [[] for _ in range(target[1] + 1)]   # można też z lewej strony ograniczyć
    for i in range(len(edge_arr)):
        if edge_arr[i][0] <= target[1] and edge_arr[i][1] <= target[1] and edge_arr[i][1] not in adj_list[edge_arr[i][0]]:
            adj_list[edge_arr[i][0]].append(edge_arr[i][1])

    return adj_list

# P = [[1, 3], [2, 3], [3, 5], [3, 7], [3, 4], [4, 8], [8, 9], [5, 7], [2, 3]]
# target = [2, 9]
# print(przerabiamy(P,target))

def BFS(G, target):
    # G = (V, E), s należy do V; w naszym przypadku G to lista sąsiedztwa
    s = target[0]
    G = przerabiamy(G, target)
    n = len(G)
    Q = Queue()
    visited = [False for _ in range(n)]

    visited[s] = True
    Q.put(s)
    while not Q.empty():
        u = Q.get()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                Q.put(v)

    return True if visited[target[1]] else False


# Zadanie 4. (sklejanie odcinków) Dany jest ciag przedziałów postaci [ai, bi]. Dwa przedziały mozna
# skleic jesli maja dokładnie jeden punkt wspólny. Prosze wskazac algorytmy dla nastepujacych problemów:

# 2. Problem stwierdzenia jaki najdłuzszy odcinek mozna uzyskac sklejajac najwyzej k odcinków.

def longest_segment(G, k):

    def DFSVisit(G, u, k, curr_len=0):
        nonlocal visited, max_len
        if curr_len > max_len:
            max_len = curr_len

        if k == 0:
            return

        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                DFSVisit(G, v, k - 1, curr_len + (v - u))

    n = len(G)
    visited = [False for _ in range(n)]
    max_len = 0
    for u in range(n):
        if not visited[u]:
            DFSVisit(G, u, k)

    return max_len


G0 = [[], [3], [3], [5, 7, 4], [8], [7], [], [], [9], []]
k0 = 4

G1 = [[], [3], [3], [5, 7], [8], [7], [], [], [9], [10], []]
k1 = 4

G2 = [[5], [2], [5], [], [], []]
k2 = 2

print(longest_segment(G0, k0))
print(longest_segment(G1, k1))
print(longest_segment(G2, k2))
#Tomek wytłumacz o co cho