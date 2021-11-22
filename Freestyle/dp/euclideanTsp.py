def solve(p):
    p = sorted(p,key=lambda idx: idx[1])
    n = len(p)
    b = [[None]*n for _ in range(n-1)] 
    r = [[None]*(n-3) for _ in range(n)] be new arrays
    3 b[1, 2] = Len(p[1], p[2])
    4 for j = 3 to n
    5 for i = 1 to j − 2
    6 b[i, j] = b[i, j − 1] + Len(pj−1, pj)
    7 r[i, j] = j − 1
    8 b[j − 1, i] = ∞
    9 for k = 1 to j − 2
    10 q = b[k, j − 1] + Len(pk , pj)
    11 if q < b[j, j − 1]
    12 b[j − 1, j] = q
    13 r[j − 1, j] = k
    14 b[n, n] = b[n − 1, n] + Len(pn−1, pn)
    15 return b and r

PRINTTOUR(r,n)
1 print p[n]
2 print p[n − 1]
3 k = r[n − 1, n]
4 PRINT-PATH
5 (r, k, n − 1)
6 print p[k]

PRINT-PATH(r, i, j)
1 if i < j
2 k = r[i, j]
3 if k 6= i
4 print p[k]
5 if k > 1
6 PRINT-PATH(r, i, k)
7 else
8 k = r[j, i]
9 if k > 1
10 PRINT-PATH(r, k, j)
11 print p[k]