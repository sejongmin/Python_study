import sys
import heapq
sys.setrecursionlimit(10 ** 9)
read = sys.stdin.readline

M, N = map(int, read().split())
graph = []
DP = [[0] * N for _ in range(M)]
q = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for _ in range(M):
    line = list(map(int, read().split()))
    graph.append(line)

q.append((-graph[0][0], 0, 0))
DP[0][0] = 1
while q:
    h, x, y = heapq.heappop(q)
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M or graph[ny][nx] >= graph[y][x]:
            continue
        if DP[ny][nx] == 0:
            heapq.heappush(q, (-graph[ny][nx], nx, ny))
        DP[ny][nx] += DP[y][x]

print(DP[M-1][N-1])