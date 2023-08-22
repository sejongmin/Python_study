import sys
read = sys.stdin.readline


N, M = map(int, read().split())

graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0
visit = [[False] * M for _ in range(N)]

for _ in range(N):
    line = list(map(int, read().split()))
    graph.append(line)

def tetrominoDFS(now, n, y, x):
    if n == 3:
        global answer
        answer = max(answer, now)
        return
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if nx < 0 or nx >= M or ny < 0 or ny >= N or visit[ny][nx]:
            continue
        visit[ny][nx] = True
        tetrominoDFS(now + graph[ny][nx], n + 1, ny, nx)
        visit[ny][nx] = False

def tetrominoEX(i, j):
    global answer

    if (i == 0 or i == N - 1):
        if (j == 0 or j == M - 1):
            return
        val = graph[i][j] + graph[i][j - 1] + graph[i][j + 1]
        if i == 0:
            val += graph[i + 1][j]
        else:
            val += graph[i - 1][j]
        answer = max(answer, val)

    elif (j == 0 or j == M - 1):
        val = graph[i][j] + graph[i - 1][j] + graph[i + 1][j]
        if j == 0:
            val += graph[i][j + 1]
        else:
            val += graph[i][j - 1]
        answer = max(answer, val)
    
    else:
        val = graph[i][j]
        for k in range(4):
            val += graph[i + dy[k]][j + dx[k]]
        for k in range(4):
            val -= graph[i + dy[k]][j + dx[k]]
            answer = max(answer, val)
            val += graph[i + dy[k]][j + dx[k]]

for i in range(N):
    for j in range(M):
        visit[i][j] = True
        tetrominoDFS(graph[i][j], 0, i, j)
        visit[i][j] = False
        tetrominoEX(i, j)

print(answer)