import sys
input = sys.stdin.readline

def solution(N, K, items):
    dp = [0] * (K + 1)
    for w, v in items:
        for i in range(K, w - 1, -1):
            dp[i] = max(dp[i], dp[i - w] + v)

    print(dp[K])

N, K = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]
solution(N, K, items)
