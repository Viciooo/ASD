def lis(M):
    n = len(M)
    M.sort()
    F = [1] * n
    P = [-1] * n
    prev = M[0][0]
    for i in range(1, n):
        for j in range(i):
            if M[j][1] < M[i][1] and F[j] + 1 > F[i] and M[j][0] != prev:
                F[i] = F[j] + 1
                P[i] = j
                prev = M[j][0]

    return max(F), P


def print_solution(A, P, i):
    if P[i] != -1:
        print_solution(A, P, P[i])

    print(A[i], end=" ")


M = [(0, 0), (1, 1), (3, 1), (1, 2), (3, 3), (6, 3.5), (2, 3), (4, 7), (7, 4)]
length, P = lis(M)
print(length)
print_solution(M, P, len(M) - 1)
# można w O(nlogn), ale nie chcę mi sie pisać :) (tak na serio to NIE)