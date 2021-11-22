from queue import PriorityQueue

def sum_oil(T):

    def go_through_stains(T, curr_i, i, j):
        nonlocal visited, res, n, m
        if not visited[i][j]:
            res[curr_i] += T[i][j]

        visited[i][j] = True
        if j + 1 < m and not visited[i][j + 1] and T[i][j + 1] != 0:
            go_through_stains(T, curr_i, i, j + 1)

        if i + 1 < n and not visited[i + 1][j] and T[i + 1][j] != 0:
            go_through_stains(T, curr_i, i + 1, j)

        if j - 1 >= 0 and not visited[i][j - 1] and T[i][j - 1] != 0:
            go_through_stains(T, curr_i, i, j - 1)

        if i - 1 >= 0 and not visited[i - 1][j] and T[i - 1][j] != 0:
            go_through_stains(T, curr_i, i - 1, j)

    n, m = len(T), len(T[0])
    res = [0 for _ in range(m)]
    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        if not visited[0][i] and T[0][i] != 0:
            go_through_stains(T, i, 0, i)

    return res

def getSolution(parent,u):
    if u == None:
        return []
    return getSolution(parent,parent[u]) + [u]


from pprint import pp, pprint

def plan(T):
    A = sum_oil(T)
    m = len(A)
    if A[0] >= m - 1:
        return [0]

    PQ = PriorityQueue()
    visited = [False for _ in range(m)]
    visited[0] = True
    for i in range(1, A[0] + 1):
        visited[i] = True
        PQ.put([-A[i], A[i] + (A[0] - i), i])

    R = [0]
    last = 0
    while not PQ.empty():
        _, span, ind = PQ.get()
        if 0 < ind < last:  # CRUCIAL
            span += last - ind + 1

        visited[ind] = True
        R.append(ind)
        last = ind
        if m - ind - 1 <= span:
            R.sort()
            return R

        for i in range(ind + 1, ind + 1 + span + 1):
            if not visited[i]:
                PQ.put([-A[i], A[i] + (span - ind), i])

    return "Piotrek gada głupoty"



T0 = [
    [1, 0],
    [0, 0],
]

T1 = [
    [3, 0, 0, 1, 0],
    [0, 1, 0, 0, 1],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
]

T2 = [
    [1, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]

T3 = [
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
    [0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

r0_T4 = [6, 0, 2, 0, 3, 0, 1, 0, 1, 0, 0, 1]
T4 = [
         r0_T4
     ] + (
             [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] * (len(r0_T4) - 1)
     )

T5 = [
    [1, 0, 1, 0, 1, 0, 0, 2, 2, 0, 0, 0],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

T6 = [
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0],
]

T7 = [
    [5, 0, 1, 0, 0, 2, 0],
    [0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0],
]

TESTS = [
    (T0, [0]),
    (T1, [0, 3]),
    (T2, [0, 4]),
    (T3, [0, 2]),
    (T4, [0, 2, 4]),
    (T5, [0, 2, 7]),
    (T6, [0]),
    (T7, [0, 5]),
]


def runtests(f):
    OK = True
    for no, (T, expected) in enumerate(TESTS):
        print(f"---------------------- #{no}")
        print("T: ")
        pprint(T)
        print(f"oczekiwany wynik: {expected}")
        assert all(len(T[i]) == len(T) for i in range(len(T))), f"len(T): {len(T)}, len(T[0]): {len(T[0])}"
        actual = f(T)
        print(f"uzyskany wynik  : {actual}")
        if actual != expected:
            print("PROBLEM!!!!!!")
            OK = False

    print("----------------------")
    if not OK:
        print("PROBLEMY!")
    else:
        print("OK")

runtests(plan)