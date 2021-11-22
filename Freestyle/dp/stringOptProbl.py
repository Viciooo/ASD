# 2. Dana jest tablica string S[n] będąca zbiorem słów oraz ciąg znaków string t. Napisz funkcję, która
# znajdzie najmniejszy taki ciąg słów ze zbioru S, aby po ich złączeniu otrzymać tekst t.


def start(S,t):
    n = len(S)
    solution = [float("inf") for _ in range(len(t))]
    for i in range()