def dawaj_wage(A):
    n = len(A)
    G = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue

            if A[i][1] < A[j][0]:
                G[i].append((j, A[j][1] - A[i][0]))

    return G


def sklej_te_przedzialy(G, k):

    def DFSVisit(G, u, k, res, falisz=0):
        nonlocal min_value, final_res
        if k == 1:
            if min_value > falisz:
                min_value = falisz
                final_res = res

            return

        for v in G[u]:
            elem = v[0]
            DFSVisit(G, elem, k - 1, res + [elem], falisz + v[1])

    G = dawaj_wage(G)
    n = len(G)
    min_value = float("inf")
    final_res = []
    for u in range(n):
        DFSVisit(G, u, k, [u])

    return final_res if final_res else bool(final_res)


A = [(1, 16), (2, 3), (4, 6), (5, 7), (9, 11), (11, 15)]
# B = [(1, 16), (2, 3)]
# C = [(1,2),(3,5),(6,8),(7,10),(8.1,8.2)]
print(sklej_te_przedzialy(A, 3))
#liczy błędne długości i co z tym zrobisz mordko hyhy
#O(V(V+E))