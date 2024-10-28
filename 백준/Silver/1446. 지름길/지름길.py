import sys
input = sys.stdin.readline

N, D = map(int, input().split())
shortcuts = []
for _ in range(N):
    shortcut = list(map(int, input().split()))
    shortcuts.append(shortcut)
shortcuts.sort(key=lambda x:-x[1])

dp = [i for i in range(D + 1)]

for i in range(1, D + 1):
    while shortcuts and shortcuts[-1][1] == i:
        s, d, l = shortcuts.pop()
        dp[i] = min(min(dp[i - 1] + 1, dp[s] + l), dp[i])
    dp[i] = min(dp[i - 1] + 1, dp[i])

print(dp[-1])