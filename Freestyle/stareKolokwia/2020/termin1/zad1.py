from random import randint, seed

def merge(T,l,r,m):
    l_copy = T[l:m+1]
    r_copy = T[m+1:r+1]

    l_idx = r_idx = 0
    sorted_idx = l

    while l_idx < len(l_copy) and r_idx < len(r_copy):
        if l_copy[l_idx] <= r_copy[r_idx]:
            T[sorted_idx] = l_copy[l_idx]
            l_idx += 1
        else:
            T[sorted_idx] = r_copy[r_idx]
            r_idx += 1
        sorted_idx += 1
    
    while r_idx < len(r_copy):
        T[sorted_idx] = r_copy[r_idx]
        sorted_idx += 1
        r_idx += 1

    while l_idx < len(l_copy):
        T[sorted_idx] = l_copy[l_idx]
        sorted_idx += 1
        l_idx += 1

    


def mergesort(T,l,r):
    if l >= r:
        return
    m = (l+r)//2
    mergesort(T,l,m)
    mergesort(T,m+1,r)
    merge(T,l,r,m)





seed(42)

n = 10
T = [ randint(1,10) for i in range(10) ]

print("przed sortowaniem: T =", T) 
mergesort(T,0,n-1)
print("po sortowaniu    : T =", T)

for i in range(len(T)-1):
    if T[i] > T[i+1]:
        print("Błąd sortowania!")
        exit()
    
print("OK")