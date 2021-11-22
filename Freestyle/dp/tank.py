def A(L,S,t):
    n = len(S)
    pos = 0
    cnt = 0
    while pos != n-1:
        dest = -1
        for i in range(pos+1,n):
            if S[i]-S[pos] <= L:
                dest = i
            else:
                break
        cnt += 1
        pos = dest
        if pos == -1:
            return -1
    if t-S[-1] > L:
        return -1
    if t == S[-1]:
        return cnt
    return cnt+1

# arr = [0,7,17,20,23,33,44]
# L = 10
# t = 44
# print(A(L,arr,t))


def C(L,S,P,t):
    n = len(S)
    F = [float("inf") for _ in range(n)]
    F[0], F[1] = 0, S[1]*P[1]
    for i in range(2,n):
        for j in range(i):
            if S[i]-S[j] > L:
                continue
            else:
                F[i] = min(F[i],(S[i]-S[j])*P[i]+F[j])
    if t - S[n-1] > L:
        return "big błąd"
    return F[n-1]

S = [0,2,3,5,7,11]
P = [0,11,7,5,3,2]
L = 5
t = 19
print(C(L,S,P,t))

def B(L, S, P, t):
    S.append(t)
    P.append(32768)
    n = len(S)
    i = 0
    curr_fuel = L
    cost = 0
    while i < n - 1:
        curr_station = i + 1    # current meaning the next one after i, not taking i into account
        min_price = float("inf")
        next_station = i
        while curr_station < n and S[curr_station] - S[i] <= L:
            if P[curr_station] < min_price:
                min_price = P[curr_station]
                next_station = curr_station

            curr_station += 1

        if next_station == n - 1:   # last jump is just weird, PW's idea, critique him
            cost += (S[n - 1] - S[i]) * P[i]

        if min_price == float("inf"):   # no ay of going to a next station, cause it's too far
            return -1

        if i == 0:    # needs to be so as not to fall for the case below
            curr_fuel = L - S[next_station]

        # theoretically there could be a waste on the last jump, but we also have to jump to t, might be a problem!!!
        elif P[i] < P[next_station]:  # when ith station has the cheapest fuel, get a full tank (if we need it)
            if next_station != n - 1:   # if we don't go to the last element
                cost += (L - curr_fuel) * P[i]

            else:   # we could move it to the condition below, but that will require changing else to elif
                cost += (S[next_station] - S[i] - curr_fuel) * P[i]

            curr_fuel = L

        # if we found a cheaper one, get the amount only needed to get to the cheaper station
        else:
            cost += (S[next_station] - S[i] - curr_fuel) * P[i]
            curr_fuel = 0

        i = next_station

    return cost

# should return -1 -- the fuel tank is too small
# L1 = 5
# S1 = [0, 2, 3, 5, 11, 17]
# P1 = [0, 45, 23, 421, 34, 35]
# print(b1(L1, S1, P1))

# should return 36 -- from 0 to 5, from 5 to 11, from 11 to 17 and the last jump to 21
# L2 = 7
# S2 = [0, 2, 3, 5, 11, 17]
# P2 = [0, 7, 9, 4, 2, 6]
# t2 = 21

print(B(L2, S2, P2, t2))