import sys
input = sys.stdin.readline

def solution(N: int, home: list) -> None:
    dp = [[[0, 0, 0] for j in range(N)] for i in range(N)]
    for i in range(1, N):
        if home[0][i] != 0:
            break
        dp[0][i][0] = 1

    for i in range(1, N):
        for j in range(1, N):
            if home [i][j] == 0 and home[i-1][j] == 0 and home[i][j-1] == 0:
                dp[i][j][1] = sum(dp[i-1][j-1])
            if home[i][j] == 0:
                dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][1]
                dp[i][j][2] = dp[i-1][j][1] + dp[i-1][j][2]

    print(sum(dp[N-1][N-1]))

N = int(input())
home = [list(map(int, input().split())) for _ in range(N)]
solution(N, home)