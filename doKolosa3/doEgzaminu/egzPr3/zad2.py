class NIEkarta:
    def __init__(self,cena,wartosc):
        self.cena = cena
        self.wartosc = wartosc
    def __str__(self) -> str:
        return str(self.cena) + "," + str(self.wartosc)

def getSolution(dp,T,i,j,k):
    if i == 0:
        if k == T[0].cena:
            return [0]
        return []

    if k >= T[i].cena and dp[i][j][k] == dp[i-1][j-1][k-T[i].cena] + T[i].wartosc:
        return getSolution(dp,T,i-1,j-1,k-T[i].cena) + [i]
    
    return getSolution(dp,T,i-1,j,k)

def starszy_pasjonat(T,x,D):
    #robimy dp[i][j][k] - max zysk z kupna j kart do itego idx wł mając k mamony
    n = len(T)
    dp = [[[0 for _ in range(D+1)] for _ in range(x+1)] for _ in range(n)]
    
    for i1 in range(n):
        if T[i1].cena <= D:
            dp[i1][1][T[i1].cena] = max(T[i1].wartosc,dp[i1][1][T[i1].cena])
            for i3 in range(i1+1,n):
                dp[i3][1][T[i1].cena] = dp[i1][1][T[i1].cena]
    
    for i in range(1,n):
        for j in range(2,x+1):
            for k in range(D+1):
                if k-T[i].cena >= 0:
                    dp[i][j][k] = max(dp[i-1][j][k],dp[i-1][j-1][k-T[i].cena]+T[i].wartosc)
    _max = 0
    for k in range(1,D+1):
        if dp[n-1][x][k] > dp[n-1][x][_max]:
            _max = k
    return getSolution(dp,T,n-1,x,_max)

from copy import deepcopy
T = [NIEkarta(5,10), NIEkarta(5,5), NIEkarta(9,1), NIEkarta(10,2)]
cp = deepcopy(T)
x = 2
D = 10
print(starszy_pasjonat(T,x,D),[cp[0],cp[1]])

T = [NIEkarta(5,10), NIEkarta(2,5), NIEkarta(4,6), NIEkarta(1,2)]
cp = deepcopy(T)
x = 3
D = 9
print(starszy_pasjonat(T,x,D),[cp[0],cp[1],cp[-1]])

