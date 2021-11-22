#algorytm ma podawać sposób wydania reszty T za pomocą nominałów z arr tak aby uzyć najmniej banknotów
def optConstruct(arr,T):
    new = [None for _ in range(T+1)]
    for i in arr:
        if i < T:
            new[i] = [i]
    for i in range(1,T):
        if new[i] != None:
            for j in range(1,i+1):
                if new[j] != None and i + j <= T:
                    if new[i+j] == None or (len(new[i+j]) > len(new[i])+len(new[j])):
                        new[i+j] = new[i] + new[j]
    return new[T]

# arr = [1,3,5,7]
# T = 21
# print(optConstruct(arr,T))

def betterSol(arr,T):
    new = [float("inf")]*(T+1)
    new[0] = 0
    sol = [-1 for _ in range(T+1)]
    for i in arr:
        if i < T:
            new[i] = 1

    for i in range(1,T+1):
        if new[i] < float("inf"):
            for j in arr:
                if i+j < T+1 and new[i]+1<new[i+j]:
                    new[i+j] = new[i]+1
                    sol[i+j] = j
    res=[None]*new[T]
    i = T
    idx = 0
    while sol[i] != -1:
        res[idx] = sol[i]
        i -= sol[i]
        idx += 1
    res[-1] = i
    return new[T],res


arr = [1,3,5,7]
T = 4
print(betterSol(arr,T))