def selectTeam(T,X):
    n = len(T)
    m = 1
    for i in range(n):
        maxi = T[i][0][0]
        for j in range(1,len(T[i])):
            if T[i][j][0] > maxi:
                maxi = T[i][j][0]
        m += maxi

    F = [[float("inf") for _ in range(m)]for _ in range(n)]
    for j in range(len(T[0])):
        F[0][T[0][j][0]] = min(T[0][j][1],F[0][T[0][j][0]])
    for i in range(1,n):
        for j in range(len(T[i])):
            for k in range(len(T[i-1])):
                if T[i-1][k][0] < float("inf"):
                    F[i][T[i][j][0]+T[i-1][k][0]] = min(F[i][T[i][j][0]+T[i-1][k][0]],T[i][j][1]+T[i-1][k][1])
                                                        #obecna                         #rozważana ze sklejenia
    for i in range(m-1,-1,-1):
        if F[n-1][i] < X:
            return F[n-1][i]
    return -1
T = [[(1,7),(2,3),(5,1)],[(3,3),(4,6),(1,2)],[(2,2),(7,7),(1,1)]]
print(selectTeam(T,15))
#lista składa się z list zawodników grających kolejno na 0,1 i 2 pozycji są reprezentowani jako (VORP,PRICE)
#zł czasowa O(n*k^2) gdzie n to ilość pozycji w dróżynie a k to średnia ilośc zawodników na pozycję - ilość zawodników 
#na pozycję może się różnić
#zł pamięciowa O(n*m) gdzie m to maksymalny VORP jaki można osiągnąć bez ograniczenia pieniężnego X
