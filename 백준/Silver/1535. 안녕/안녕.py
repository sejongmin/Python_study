import sys
input = sys.stdin.readline

def solution(N, h, p):
    dp = [[0] * 100 for _ in range(N)]
    for i in range(h[0], 100):
        dp[0][i] = p[0]

    for i in range(1, N):
        for j in range(100):
            if j >= h[i]:
                dp[i][j] = max(dp[i - 1][j], dp[i-1][j-h[i]] + p[i])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[N-1][-1]

N = int(input())
h = list(map(int, input().split()))
p = list(map(int, input().split()))
print(solution(N, h, p))
