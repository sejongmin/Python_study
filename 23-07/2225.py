import sys
read = sys.stdin.readline
limit = int(10e8)

N, K = map(int, read().split())
DP = [[0] * (N + 1) for _ in range(K + 1)]
DP[1] = [1] * (N + 1)


for i in range(2, K + 1):
    DP[i][0] = 1
    for j in range(1, N + 1):
        DP[i][j] = DP[i - 1][j] + DP[i][j - 1]
        
print(DP[K][N] % limit)
