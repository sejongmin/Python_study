import sys
input = sys.stdin.readline

def solution(N, M, mat):
    INF = 600
    dp = [[[INF, INF, INF] for i in range(M)] for j in range(N)]
    for i in range(M):
        for j in range(3):
            dp[0][i][j] = mat[0][i]

    for i in range(1, N):
        for j in range(M):
            if j < M - 1:
                dp[i][j][0] = min(dp[i - 1][j + 1][1], dp[i - 1][j + 1][2]) + mat[i][j]
            dp[i][j][1] = min(dp[i - 1][j][0], dp[i - 1][j][2]) + mat[i][j]
            if j > 0:
                dp[i][j][2] = min(dp[i - 1][j - 1][0], dp[i - 1][j - 1][1]) + mat[i][j]

    answer = INF
    for i in range(M):
        answer = min(answer, min(dp[N - 1][i]))
    
    return answer

N, M = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, M, mat))