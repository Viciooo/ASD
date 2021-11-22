# Zadanie 1. (Black Forest) Black Forest to las rosnący na osi liczbowej gdzieś w południowej Anglii. Las
# składa się z n drzew rosnących na pozycjach 0, . . . , n−1. Dla każdego i ∈ {0, . . . , n−1} znany jest zysk ci
# , jaki
# można osiągnąć ścinając drzewo z pozycji i. John Lovenoses chce uzyskać maksymalny zysk ze ścinanych
# drzew, ale prawo zabrania ścinania dwóch drzew pod rząd. Proszę zaproponować algorytm, dzięki któremu
# John znajdzie optymalny plan wycinki.

def f(i):
    global V
    if i in memoF:
        return memoF[i]
    if i == 0:
        memoF[i] = V[0]
        return memoF[i]
    memoF[i] = g(i-1) + V[i]
    return memoF[i]


def g(i):
    global V
    if i in memoG:
        return memoG[i]
    if i == 0:
        memoG[i] = 0
        return memoG[i]
    memoG[i] = max(f(i-1),g(i-1))
    return memoG[i]

V = [2,3,5,7,1,11,13,0,0,17]
memoG = {}
memoF = {}
print(g(len(V)))