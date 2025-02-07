import sys
input = sys.stdin.readline

def solution(N: int, houses: list) -> int:
    INF = 1000
    answer = INF * INF
    dp = [[0, 0, 0] for _ in range(N)]
    for k in range(3):
        dp[0] = [INF, INF, INF]
        dp[0][k] = houses[0][k]
        for i in range(1, N - 1):
            dp[i][0] = houses[i][0] + min(dp[i-1][1], dp[i-1][2])
            dp[i][1] = houses[i][1] + min(dp[i-1][0], dp[i-1][2])
            dp[i][2] = houses[i][2] + min(dp[i-1][0], dp[i-1][1])

        dp[N - 1][k] = INF * INF
        dp[N - 1][k - 1] = houses[N - 1][k - 1] + min(dp[N - 2][k], dp[N - 2][k - 2])
        dp[N - 1][k - 2] = houses[N - 1][k - 2] + min(dp[N - 2][k], dp[N - 2][k - 1])

        answer = min(answer, min(dp[N - 1]))
    return answer

N = int(input())
houses = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, houses))
