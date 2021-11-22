# Zadanie 3. (uniwersalne ujscie) Mówimy, ze wierzchołek t w grafie skierowanym jest uniwersalnym
# ujsciem, jesli (a) z kazdego innego wierzchołka v istnieje krawedz z v do t, oraz (b) nie istnieje zadna krawedz
# wychodzaca z t. Prosze podac algorytm znajdujacy ujscie (jesli istnieje) przy reprezentacji macierzowej grafu.

def check(G):#jakby się komuś chciało to mozna w miejscu i na bieżąco bez zapisywania sprawdzać
    n = len(G)
    rows = [0]*n
    cols = [0]*n
    for r in range(n):
        for c in range(n):
            rows[r] += G[r][c]
            cols[c] += G[r][c]
    for i in range(n):
        if cols[i] == n-1:
            if rows[i] == 0:
                return True
    return False

G = [[0,1,0,1],
    [0,0,0,1],
    [0,0,0,1],
    [0,0,0,0]]
print(check(G))