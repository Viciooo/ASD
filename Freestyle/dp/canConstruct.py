def isPrefix(word,candidate,idx):
    if len(candidate) > len(word)-idx:
        return -1
    for i in range(idx,idx+len(candidate)):
        if word[i] != candidate[i-idx]:
            return -1
    return idx+len(candidate)

def bfSolution(target,wordBank,idx=0):
    if idx >= len(target):
        return True
    for i in wordBank:
        tmp = isPrefix(target,i,idx)
        if tmp != -1 and bfSolution(target,wordBank,tmp):
            return bfSolution(target,wordBank,tmp)
    return False

def dpSolution(target,wordBank,idx=0,memo=[]):
    if idx in memo:
        return False
    if idx >= len(target):
        return True
    for i in wordBank:
        tmp = isPrefix(target,i,idx)
        if tmp != -1 and dpSolution(target,wordBank,tmp,memo):
            return dpSolution(target,wordBank,tmp,memo)
    memo.append(idx)
    return False

# print(dpSolution("aaaaaaaaaaaaaaaaaaaaaaaanaaaaaabbbbb",["aa","aa","a","bbb","b","n","bbbb"]))

def by1stLttrSort(arr):
    buckets = [[] for _ in range(26)]
    for i in arr:
        buckets[ord(i[0])-ord('a')].append(i)
    return buckets

def dpBetterSolution(target,wordBank,idx=0,memo=[]):
    if idx in memo:
        return False
    if idx >= len(target):
        return True
    for i in wordBank[ord(target[idx])-ord('a')]:
        tmp = isPrefix(target,i,idx)
        if tmp != -1 and dpBetterSolution(target,wordBank,tmp,memo):
            return dpBetterSolution(target,wordBank,tmp,memo)
    memo.append(idx)
    return False

def runSolution(target,wordBank):
    wordBank = by1stLttrSort(wordBank)
    return dpBetterSolution(target,wordBank)

#n = len(target)
#m = len(wordBank)
#czasowo O(26+m+n*m*m) (?)
#pamięciowo O(m+m)
# print(runSolution("aaaaaaaaaaaaaaaaaaaaaaaanaaaaaabbbbb",["aa","aa","a","bbb","b","n","bbbb"]))