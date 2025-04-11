import sys
input = sys.stdin.readline

def solution(s):
    n = len(s)
    p = [[False if i != j else True for j in range(n)] for i in range(n)]
    dp = [2500] * (n + 1)

    for i in range(n - 1):
        if s[i] == s[i + 1]:
            p[i][i + 1] = True

    for i in range(2, n):
        for j in range(n - i):
            if p[j + 1][j + i - 1] and s[j] == s[j + i]:
                p[j][j + i] = True
    
    dp[-1] = 0
    for end in range(n):
        for start in range(end + 1):
            if p[start][end]:
                dp[end] = min(dp[end], dp[start - 1] + 1)
            else:
                dp[end] = min(dp[end], dp[end - 1] + 1)

    return dp[n-1]

s = input().strip()
print(solution(s))
    