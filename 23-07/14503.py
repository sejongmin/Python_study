import sys
read = sys.stdin.readline

graph = []
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
q = []
answer = 0

N, M = map(int, read().split())
y, x, dir = map(int, read().split())
q.append((x, y))
for _ in range(N):
    line = list(map(int, read().split()))
    graph.append(line)

while q:
    x, y = q.pop(0)
    if graph[y][x] == 0:
        graph[y][x] = 2
        answer += 1
    for i in range(dir - 1, dir - 5, -1):
        nx, ny = x + dx[(i + 4) % 4], y + dy[(i + 4) % 4]
        if nx < 0 or nx >= M or ny < 0 or ny >= N or graph[ny][nx] != 0:
            continue
        q.append((nx, ny))
        dir = (i + 4) % 4
        break

    if len(q) == 0:
        nx, ny = x + dx[(dir + 2) % 4], y + dy[(dir + 2) % 4]
        if nx < 0 or nx >= M or ny < 0 or ny >= N or graph[ny][nx] == 1:
            break
        q.append((nx, ny))

print(answer)