def countSortWords(arr,pos):
    #dla uproszczenia zakładam że litery są małe i każde słowo jest równie długie
    letters = [0]*26
    n = len(arr)
    new = [0]*n
    for i in arr:
        l = ord(i[pos]) - ord('a')
        letters[l] += 1
    for i in range(1,26):
        letters[i] += letters[i-1]
    for i in range(n-1,-1,-1):
        l = ord(arr[i][pos]) - ord('a')
        letters[l] -= 1
        new[letters[l]] = arr[i]
    for i in range(n):
        arr[i] = new[i]

def radixSortWords(arr):
    size = len(arr[0])
    for i in range(size-1,-1,-1):
        countSortWords(arr,i)

arr = ["ab","ze","ef","ii","jk"]
radixSortWords(arr)
print(arr)