# Dana jest tablica A mająca n liczb naturalnych przyjmujących wartości z zakresu [0...n].
# Proszę napisać algorytm znajdujący rozmiar największego podzbioru liczb z A,
# takiego, że ich GCD jest różny od 1. Algorytm powinien działać jak najszybciej.

def getPrimeDiv(n):
    i= 2
    div = []
    tmp = n
    while i <= n:
        if tmp % i == 0:
            div.append(i)
            while tmp % i == 0:
                tmp //= i
        else:
            i += 1
    return div

def ex10(arr):
    n = len(arr)
    for i in range(n):
        arr[i] = (arr[i],getPrimeDiv(arr[i]))
    count = [0 for i in range(n)]
    for i in range(n):
        for div in arr[i][1]:
            count[div] += 1
    maxi = 0
    for i in range(1,n):
        if count[maxi] < count[i]:
            maxi = i
    S = []
    for i in range(n):
        if maxi in arr[i][1]:
            S.append(arr[i][0])
    return S
