def solve(T):
    n = len(T)
    F = [1]*n
    def travel(T,s):
        for v in T[s]:
            travel(T,v)
            F[s] += F[v]
    travel(T,0)
    return F

T=[[1,2],[3,4,5],[6,7],[],[],[],[],[8],[]]
print(solve(T))
        