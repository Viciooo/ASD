# Zadanie 5. (maximin) Rozwazmy ciag (a0, . . . , an−1) liczb naturalnych. Załózmy, ze został podzielony
# na k spójnych podciagów: (a0, . . . , a`1), (a`1+1, . . . , a`2), . . . , (a`k−1+1, . . . , an−1). Przez wartosc i-go podciagu
# rozumiemy sume jego elementów a przez najgorszy podciag rozumiemy podciag o najmniejszej wartosci (rozstrzygajac
# remisy w dowolny sposób). Wartoscia podziału jest wartosc jego najgorszego podciagu. Zadanie
# polega na znalezienie podziału ciagu (a0, . . . , an−1) o maksymalnej wartosci.

def maxmin(arr,T):
    n = len(arr)
    F = [[-float("inf") for _ in range(n)] for _ in range(T)]
    _sum = 0
    for i in range(n):
        _sum += arr[i]
        F[0][i] = _sum
    for t in range(1,T):
        for i in range(t,n):
            for j in range(i):
                F[t][i] = max(min(F[t-1][j],F[0][i]-F[0][j]),F[t][i])
    return F[T-1][n-1]
arr = [5,6,1,3,12]
T = 3
print(maxmin(arr,T))
#jest git kurwaza