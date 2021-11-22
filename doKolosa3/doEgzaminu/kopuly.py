def provideCityWithSafety(arr,x):
    n = len(arr)
    arr.sort()
    print(arr)
    F = [float("inf") for _ in range(n)]
    for i in range(n):
        if arr[i][0] == 0:
            F[i] = arr[i][2]

    for i in range(n):
        for j in range(i):
            if arr[i][0] == arr[j][1]:
                F[i] = min(F[i],F[j]+arr[i][2])

    _min = float("inf")
    for i in range(n):
        if arr[i][1] >= x:
            _min = min(_min,F[i])
    return _min if _min != float("inf") else None

T = [(0,2,4), (0,1,1), (4,8,1), (1,9,1), (8,10,2), (2,5,2)]
x = 10
odp = None
print(provideCityWithSafety(T,x))

T = [(0,1,1), (0,2,4), (1,9,1), (2,8,1), (8,10,2), (8,10,5), (9,10,2)]
x = 10
print(provideCityWithSafety(T,x))

poczatek_parku_koniec_parku1 = 10
T1 = [(3,4,2),(2.5,5.5,1),(9,10,888),(0,1,2),(0,2.5,1),(7,9,4),(1,3,6),(8,11,8),(4,8,64),(5.5,7,3)]
odp : 82
print(provideCityWithSafety(T1,poczatek_parku_koniec_parku1))

poczatek_parku_koniec_parku = 1
T = [(0,0.4,1),(0,1,1500),(0.5,1,1)]
print(provideCityWithSafety(T,poczatek_parku_koniec_parku))

#zł O(n^2)
#zakładając że kopuły są różnej długości