import sys
import heapq
INF = int(1e9)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
answer = []

read = sys.stdin.readline

while True:
    N = int(read())
    if N == 0:
        break
    q = []
    graph = []
    dist = [[INF for i in range(N)] for j in range(N)]

    for _ in range(N):
        line = list(map(int, read().split()))
        graph.append(line)
    
    heapq.heappush(q, (graph[0][0], 0, 0))

    while q:
        cost, x, y = heapq.heappop(q)
        if dist[y][x] > cost:
            dist[y][x] = cost
            if y == N-1 and x == N-1:
                break
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue
                if cost + graph[ny][nx] < dist[ny][nx]:
                    heapq.heappush(q, (cost + graph[ny][nx], nx, ny))
    answer.append(dist[N-1][N-1])

for i, val in enumerate(answer):
    print("Problem %d: %d" %(i+1, val))