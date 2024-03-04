def solution(n, money):
    dp = [1] + [0] * n
    money.sort()
    for m in money:
        for i in range(m, n + 1):
            dp[i] += dp[i - m]
    return dp[n]