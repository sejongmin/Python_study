import sys
input = sys.stdin.readline

def solution(N):
    if N == 1:
        print(3)
        return
    elif N == 2:
        print(7)
        return
    dp = [1] * (N + 1)
    dp[1] = 3
    dp[2] = 7

    for i in range(3, N + 1):
        dp[i] = (2 * dp[i - 1] + dp[i - 2]) % 9901

    print(dp[-1])

N = int(input())
solution(N)