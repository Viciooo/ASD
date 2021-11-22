from queue import PriorityQueue
#zł obliczeniowa O(ElogV)
#zł pamięciowa O(V)
def travel_guide(G, s, e):
    n = len(G)
    Q = PriorityQueue()
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    d = [0 for _ in range(n)]
    d[s] = float("inf")

    Q.put([0, 0, s])
    # [klucz, rzeczywista waga, wierzchołek]
    # rzeczywista waga = min(krawędź do wierzchołka, waga wierzchołka, z którego idziemy)
    while not Q.empty():
        u = Q.get()
        if not visited[u[2]]:
            visited[u[2]] = True
            for v in G[u[2]]:
                mini = min(d[u[2]], v[1])
                if d[v[0]] < mini:
                    parent[v[0]] = u[2]
                    d[v[0]] = mini

                Q.put([-d[v[0]], d[v[0]], v[0]])

    return print_solution(parent, e)


def print_solution(parent, i):
    if parent[i] is None:
        print(i, end=" ")
        return

    print_solution(parent, parent[i])
    print(i, end=" ")


G = [[[1, 10 ** 6], [2, 100]],
     [[0, 10 ** 6], [4, 1]],
     [[0, 100], [3, 100]],
     [[2, 100], [4, 100]],
     [[1, 1], [3, 100]]]

G1 = [[[1, 10 ** 6], [2, 100]],
      [[3, 1]],
      [[4, 100]],
      [[6, 10]],
      [[5, 100]],
      [[3, 100]],
      [[7, 15]],
      []
      ]

travel_guide(G, 0, 4)
print()
travel_guide(G1, 0, 7)