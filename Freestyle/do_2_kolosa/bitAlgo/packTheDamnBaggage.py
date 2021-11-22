"""
f(i, s) = czy można otrzymać sumę s, dodając elementy od a_0 do a_i-1 <- do tego włącznie.
f(i, 0) = True
f(0, A[0]) = True, wpp. dla s != A[0] f(0, s) = False
f(i, s) = f(i - 1, s) or f(i - 1, s - A[i - 1])
"""

def pack_the_damn_baggage(B, W):
    if W % 2 == 1:
        return False

    W //= 2
    N = len(B)
    F = [[False for _ in range(W + 1)] for _ in range(N + 1)]
    for i in range(N + 1):
        F[i][0] = True

    for i in range(1, N + 1):
        for j in range(1, W + 1):
            F[i][j] = F[i - 1][j]
            if W >= B[i - 1]:
                F[i][j] = F[i - 1][j] or F[i - 1][W - B[i - 1]]

    return F[N][W]


B = [2, 5, 7, 11, 13]
test1 = sum(B)
C = [2, 3, 5, 10]
test2 = sum(C)

print(pack_the_damn_baggage(B, test1))
print(pack_the_damn_baggage(C, test2))