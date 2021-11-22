def solve(T):
    n = len(T)
    T.sort(key= lambda x: x[1],reverse=True)
    T.sort(key= lambda x: x[0])
    solution = [T[0]]
    j = 0
    for i in range(1,n):
        if T[i][1] <= solution[j][1]:
            continue
        elif j != 0 and T[i][0] <= solution[j-1][1] and T[i][1] > solution[j][1]:
            solution[j] = T[i]
        elif T[i][0] <= solution[j][1]:
            solution.append(T[i])
            j += 1
        else:
            return None
    if solution[-1][1] < 1:#przy zał że przedziały od [0,1]
        return None
    return solution
T1 = [(0,4),(1,5),(0,2),(3,7),(7,10)]
odp1 = [(0, 4), (3, 7), (7, 10)]
print(solve(T1))

T2 = [(0,4),(1,5),(0,2),(7,10)]
odp2 = None
print(solve(T2))

T3 = [(0,4),(1,5),(0,2),(3,7),(7,10),(0,3),(7,8),(8,10)]
odp3 = [(0, 4), (3, 7), (7, 10)]
print(solve(T3))

T4 = [(0,5),(1,6),(2,7),(3,8),(4,9),(5,10)]
odp4 = [(0, 5), (5, 10)]
print(solve(T4))

T0 = [(0.88, 1),(0.65, 0.9),(0,0.15), (0.2, 0.4),(0.1, 0.7), (0.13, 0.85), (0, 0.3)]
odp = 4
print("odp:",solve(T0))

T1 = [(0.65, 0.9),(0,0.15), (0.2, 0.4),(0.1, 0.7), (0.13, 0.85), (0, 0.3)]
odp = False
print("odp:",solve(T1))