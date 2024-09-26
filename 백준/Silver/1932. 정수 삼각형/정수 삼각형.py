import sys
input = sys.stdin.readline

def solution(n):
    dp = [[0] * i for i in range(1, n + 1)]
    triangle = []
    for _ in range(n):
        triangle.append(list(map(int, input().split())))

    dp[0][0] = triangle[0][0]
    for i in range(1, n):
        dp[i][0] = triangle[i][0] + dp[i - 1][0]
        dp[i][i] = triangle[i][i] + dp[i - 1][i - 1]
        for j in range(1, i):
            dp[i][j] = triangle[i][j] + max(dp[i - 1][j], dp[i - 1][j - 1])
            
    return max(dp[-1])

n = int(input())
print(solution(n))