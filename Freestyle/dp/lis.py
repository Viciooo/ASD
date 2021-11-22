def findIdxOfMax(arr):
    maxi = arr[0]
    for i in range(1,len(arr)):
        if arr[i] > arr[maxi]:
            maxi = i
    return maxi

def lis(arr):
    n = len(arr)
    F = [1 for _ in range(n)]
    P = [-1 for _ in range(n)]
    for i in range(1,n):
        for j in range(i):
            if arr[j] < arr[i] and F[i] < F[j]+1:
                F[i] = F[j]+1
                P[i] = j
    return P

def printLis(A,P,i):
    if P[i] >= 0:
        printLis(A,P,P[i])
    print(A[i],end=' ')

arr = [3,4,-1,5,8,2,3,12,7,9,10]
P = lis(arr)
printLis(arr,P,findIdxOfMax(P))