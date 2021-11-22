def cutRod(arr):
    n = len(arr)
    for i in range(2,n):
        for j in range(1,(i//2)+1):
            arr[i] = max(arr[i],arr[j]+arr[i-j])
    return arr[-1]

#optymalizacyjny problem rozwiązalibyśmy nową tablicą i zastępując elementy pojedynczymi tablicami
#      [0,1,2,3,4,5,6,7,8,9,10]
arr = [0,3,5,8,9,10,17,17,20]
print(cutRod(arr))
#zł czasowa O(1+2+2+3+3+4+4+...n//2+n//2)
#O(1+2*(2+n//2)/2*(n//2-1)) = O(n^2)
#pamięciowa O(1)