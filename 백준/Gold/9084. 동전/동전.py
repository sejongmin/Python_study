import sys
input = sys.stdin.readline

def solution(N, coins, price):
    coins = [0] + coins
    dp = [[1] + [0] * price for _ in range(N + 1)]

    for i in range(1, N + 1):
        if coins[i] > price:
            print(dp[i - 1][-1])
            return
        for j in range(1, coins[i]):
            dp[i][j] = dp[i - 1][j]
        for j in range(coins[i], price + 1):
            dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i]]
    print(dp[N][-1])

T = int(input())
for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    price = int(input())
    solution(N, coins, price)