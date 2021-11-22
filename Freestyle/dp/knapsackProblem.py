
def get_solution(F, W, P, i, w):
    if i == 0:
        if w >= W[0]:
            return [0]

        return []

    if w >= W[i] and F[i][w] == F[i - 1][w - W[i]] + P[i]:
        return get_solution(F, W, P, i - 1, w - W[i]) + [i]

    return get_solution(F, W, P, i - 1, w)

def knapsack(W, P, MaxW):
    n = len(W)
    F = [[0 for _ in range(MaxW + 1)] for _ in range(n)]

    for w in range(W[0], MaxW + 1):
        F[0][w] = P[0]

    for i in range(1, n):
        for w in range(1, MaxW + 1):
            F[i][w] = F[i - 1][w]
            if w >= W[i]:
                F[i][w] = max(F[i][w], F[i - 1][w - W[i]] + P[i])

    # return get_solution(F,W,P,len(P)-1,maxW)
    return F[n-1][MaxW]

P = [10, 8, 4, 5, 3, 7]
W = [4, 5, 12, 9, 1, 13]
MaxW = 15
print(knapsack(W, P, MaxW))
# O(n*Σ(od i = 0 do n - 1) P[i])
def knapsack_little_change_in_the_code(W, P, MaxW):
    n = len(W)
    P_sum = sum(P)
    profits = [-1 for _ in range(P_sum + 1)]
    for i in range(n):
        for j in range(P_sum, P[i], -1):
            if profits[j - P[i]] != -1:
                if profits[j] == -1:
                    profits[j] = profits[j - P[i]] + W[i]

                else:
                    profits[j] = min(profits[j], profits[j - P[i]] + W[i])

        if profits[P[i]] == -1:
            profits[P[i]] = W[i]

        else:
            profits[P[i]] = min(W[i], profits[P[i]])

    for i in range(P_sum, -1, -1):
        if profits[i] != -1 and profits[i] < MaxW:
            return i


P = [10, 8, 4, 5, 3, 7]
W = [4, 5, 12, 9, 1, 13]
MaxW = 15
print(knapsack_little_change_in_the_code(W, P, MaxW))
