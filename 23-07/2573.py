import sys
read = sys.stdin.readline

graph = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, read().split())

for _ in range(N):
    line = list(map(int, read().split()))
    graph.append(line)

year = 0

while True:
    visit = [[0] * M for _ in range(N)]
    melt = [[0] * M for _ in range(N)]
    q = []
    count = 0

    for i in range(1, N-1):
        for j in range(1, M-1):
            if graph[i][j] > 0 and visit[i][j] == 0:
                count += 1
                q.append((i, j))
                visit[i][j] = 1
                while q:
                    y, x = q.pop(0)
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if graph[ny][nx] > 0 and visit[ny][nx] == 0:
                            q.append((ny, nx))
                            visit[ny][nx] = 1
                        elif graph[ny][nx] < 1:
                            melt[y][x] += 1
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            graph[i][j] -= melt[i][j]

    if count > 1:
        Flag = 1
        break
    if count == 0:
        Flag = 0
        break
    year += 1

if Flag:
    print(year)
else:
    print(0)