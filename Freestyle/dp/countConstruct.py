def isPrefix(word,candidate,idx):
    if len(candidate) > len(word)-idx:
        return -1
    for i in range(idx,idx+len(candidate)):
        if word[i] != candidate[i-idx]:
            return -1
    return idx+len(candidate)

def by1stLttrSort(arr):
    buckets = [[] for _ in range(26)]
    for i in arr:
        buckets[ord(i[0])-ord('a')].append(i)
    return buckets


# def runSolution(target,wordBank):
#     total = 0
#     wordBank = by1stLttrSort(wordBank)
#     def dpBetterSolution(target,wordBank,idx=0,memo=[]):
#         nonlocal total
#         # for i in memo:
#         #     if i[0] == idx:
#         #         if i[1] == 1:
#         #             total += 1
#         #             return True
#         #         else:
#         #             return False
#         if idx == len(target):
#             total += 1
#             return True
#         for i in wordBank[ord(target[idx])-ord('a')]:
#             tmp = isPrefix(target,i,idx)
#             if tmp != -1 and dpBetterSolution(target,wordBank,tmp,memo):
#                 dpBetterSolution(target,wordBank,tmp,memo)
#                 memo.append((idx,1))
#         memo.append((idx,0))
#         return False
#     dpBetterSolution(target,wordBank)
#     return total

# print(runSolution("abcdeefgee",["ab","cd","ee","e","fg","fgee"]))

#działa źle