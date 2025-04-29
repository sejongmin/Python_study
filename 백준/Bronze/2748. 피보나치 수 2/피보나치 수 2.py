import sys
input = sys.stdin.readline

def solution(N):
    dp = [0 for i in range(N + 1)]
    dp[1] = 1

    for i in range(2, N + 1):
        dp[i] = dp[i - 2] + dp[i - 1]

    return dp[N]

N = int(input())
print(solution(N))
