def howManyWays(A):
    n = len(A)
    F = [0]*n
    F[0] = 1
    for i in range(n):
        for j in range(1,A[i]+1):
            if i+j < n:
                F[i+j] += F[i]
    return F

# A = [1,3,2,1,0]
# #i think iit works but it may need further testing
# print(howManyWays(A))

def getSolution(F,i,res):
    if i == 0:
        print(res[::-1])
        return
    for j in F[i]:
        getSolution(F,j,res+str(j))

def inWhatWays(A):
    n = len(A)
    F = [[] for _ in range(n)]
    for i in range(n):
        for j in range(1,A[i]+1):
            if i+j < n:
                F[i+j].append(i)
    return getSolution(F,n-1,str(n-1))


A = [1,3,2,1,0]
#i think iit works but it may need further testing
inWhatWays(A)