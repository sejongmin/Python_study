import sys
read = sys.stdin.readline

N = int(read().strip())
boxes = list(map(int, read().split()))
DP = [1 for _ in range(N)]

for i in range(1, N):
    max_DP = 0
    for j in range(i - 1, -1, -1):
        if boxes[i] > boxes[j] and max_DP < DP[j]:
            max_DP = DP[j]
    DP[i] = max_DP + 1

print(max(DP))