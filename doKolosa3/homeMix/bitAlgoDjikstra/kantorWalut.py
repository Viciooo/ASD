from math import log2


def search_for_index(C, n, u):  # u -- string z walutą
    for i in range(n):
        if u == C[i]:
            return i


def change_to_list(G, C):
    n = len(C)
    L = []
    for i in range(len(G)):
        a, b, w = G[i]
        u = search_for_index(C, n, a)
        v = search_for_index(C, n, b)
        L.append([u, v, -log2(w)])

    return L


def exchange_currency(G, a, b):
    C = []
    for u, v, w in G:
        if u not in C:
            C.append(u)

        if v not in C:
            C.append(v)

    n = len(C)
    print(C)
    L = change_to_list(G, C)
    parent = [None for _ in range(n)]
    d = [float("inf") for _ in range(n)]

    u = search_for_index(C, n, a)
    d[u] = 0
    for i in range(n - 1):
        for u, v, w in L:
            if d[v] > d[u] + w:  # we want to maximize the result
                d[v] = d[u] + w
                parent[v] = u

    arbitrage = False
    for u, v, w in L:
        if d[v] > d[u] + w:
            arbitrage = True

    v = search_for_index(C, n, b)
    return get_solution(parent, C, u, v) if not arbitrage else arbitrage


def get_solution(parent, C, c1, i):
    if parent[i] is None:
        return [C[i]]

    return get_solution(parent, C, c1, parent[i]) + [C[i]]


F = [
    ("EUR", "PLN", 0.22),
    ("PLN", "EUR", 4.46),
    ("USD", "PLN", 0.27),
    ("PLN", "USD", 3.36),
    ("EUR", "USD", 0.82),
    ("USD", "EUR", 1.21)
]

# EURO    PLN     USD
# 0       1       2
print(exchange_currency(F, "PLN", "EUR"))
print(exchange_currency(F, "EUR", "PLN"))
# print(exchange_currency(F, 2, 0))
# print(exchange_currency(F, 0, 2))
# print(exchange_currency(F, 1, 2))
# print(exchange_currency(F, 2, 1))