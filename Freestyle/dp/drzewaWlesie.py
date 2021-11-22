# 1. W lesie znajduje się n drzew stojących w jednej linii. Każde drzewo posiada określoną wartość, która
# należy traktować jako zysk po jego wycięciu. Nie możemy wyciąć więcej niż dwóch drzew pod rząd.
# Proszę zaimplementować funkcję pozwalającą określić które drzewa należy wyciąć, aby sumaryczny zysk
# był jak największy. 

best = 0
def bfSolution(arr,n,i,curr=0):
    global best
    if i >= n:
        best = max(best,curr)
        return
    return bfSolution(arr,n,i+2,curr+arr[i]) or bfSolution(arr,n,i+3,curr+arr[i])

arr = [2,10,4,1,17,3,5]
bfSolution(arr,len(arr),0)
bfSolution(arr,len(arr),1)
print(best)