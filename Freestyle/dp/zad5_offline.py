def lis(arr):
    n = len(arr)
    F = [1 for _ in range(n)]
    P = [-1 for _ in range(n)]
    S = [[-1] for _ in range(n)]
    for i in range(1,n):
        for j in range(i):
            if arr[j] < arr[i] and F[i] < F[j]+1:
                F[i] = F[j]+1
                P[i] = j
                S[i] = [j]
            elif arr[j] < arr[i] and F[i] == F[j]+1:
                S[i] += [j]
    return P,S

def printAllLis(A):
    P,S = lis(A)
    maxi = max(P)
    n = len(P)
    ret = 0
    def foo(A,S,i,res=""):
        if i == -1:
            print(res)
            return 1
        ret = 0
        for j in S[i]:
            ret += foo(A,S,j,str(A[i]) + ' ' + res)
        return ret

    for i in range(n):
        if P[i] == maxi:
            ret += foo(A,S,i)
    return ret

A = [2,1,4,3,7]
print(printAllLis(A))