import sys
input = sys.stdin.readline

def solution(N, M, companys):
    dp = [0 for _ in range(N + 1)]
    invest = [[0 for _ in range(M)] for i in range(N + 1)] # 총투자액 -> 기업

    now = 0
    for i in range(N):
        dp[i + 1] = companys[i][1]
        invest[i + 1][0] = i + 1

    for i in range(2, M + 1):
        for j in range(N, 0, -1):
            for k in range(j, 0, -1):
                if dp[j] < dp[j - k] + companys[k - 1][i]:
                    dp[j] = dp[j - k] + companys[k - 1][i]
                    invest[j] = invest[j - k][:]
                    invest[j][i - 1] = k

    print(dp[-1])
    print(*invest[-1])
        

N, M = map(int, input().split())
companys = [list(map(int, input().split())) for _ in range(N)]
solution(N, M, companys)