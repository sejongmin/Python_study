import sys
read = sys.stdin.readline

N = int(read())
graph = []

for _ in range(N):
    line = list(map(int, read().split()))
    graph.append(line)


def solution():
    DP = [[0] * N for _ in range(N)]
    DP[0][0] = 1

    for i in range(N):
        for j in range(N):
            if i == j == N-1:
                return DP[N-1][N-1]
            cost = graph[i][j]
            if i + cost < N:
                DP[i + cost][j] += DP[i][j]
            if j + cost < N:
                DP[i][j + cost] += DP[i][j]

print(solution())