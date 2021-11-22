# Zadanie 2. (spadające klocki) Każdy klocek to przedział postaci [a, b]. Dany jest ciąg klocków [a1, b1],
# [a2, b2], . . ., [an, bn]. Klocki spadają na oś liczbową w kolejności podanej w ciągu. Proszę zaproponować
# algorytm, który oblicza ile klocków należy usunąć z listy tak, zeby każdy kolejny spadajacy klocek mieścił
# się w całości w tam, który spadł tuż przed nim.


A = [(1,1), (1,10), (3,8), (1,5), (8,9), (8.5, 9), (5,6)] # 2

n = len(A)

F = [1]*n

for i in range(1, n):
    for j in range(i):
        a1, b1 = A[i]
        a2, b2 = A[j]
        if a1 >= a2 and b1 <= b2:
            F[i] = max(F[i], F[j] + 1)

print(n-max(F))