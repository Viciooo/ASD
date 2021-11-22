class Job:
    def __init__(self,start=0,end=0):
        self.start = start
        self.end = end
    def __str__(self):
        return "( " + str(self.start) + " - " + str(self.end) + " )"

# dp[i][j] = minimalny czas aby sposrod pierwszych i rzeczy wziac j rzeczy i na pewno w nich musi byc i
# to jest chujnia japierdole O(n^2 * k) :(((((((
# no i git co by wiecej pisac, to taki stos najwyzszy z zajec konczac na itym o wysokosci j

def impatientBobby(J,n,k):
    dp = [[float('inf') for _ in range(k+1)]for _ in range(n)]
    for i in range(n):
        dp[i][1] = 0
        for l in range(i):
            if J[i].start >= J[l].end:
                for j in range(1,k):
                    if dp[l][j] < float('inf'):
                        dp[i][j+1] = min(dp[i][j+1], dp[l][j] +  J[i].start-J[l].end)
            else:
                continue
    mini = float('inf')
    for i in range(n):
        if dp[i][k] < float('inf') and dp[i][k] < mini:
            mini = dp[i][k]

    return mini if mini < float('inf') else -1
