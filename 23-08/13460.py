import sys
read = sys.stdin.readline

N, M = map(int, read().split())
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
rx, ry, bx, by = 0, 0, 0, 0
visit = [[[[False] * M for i in range(N)] for j in range(M)] for k in range(N)]

for _ in range(N):
    line = list(read().strip())
    if 'R' in line:
        rx, ry = line.index('R'), _
    if 'B' in line:
        bx, by = line.index('B'), _
    graph.append(line)

def move(x, y, dx, dy):
    moveCnt = 0
    while graph[y + dy][x + dx] != '#' and graph[y][x] != 'O':
        x = x + dx
        y = y + dy
        moveCnt += 1
    return x, y, moveCnt

q = []
q.append((rx, ry, bx, by, 1))
visit[ry][rx][by][bx] = True

def BFS():
    while q:
        rx, ry, bx, by, depth = q.pop(0)
        if depth > 10:
            print(-1)
            return
        for i in range(4):
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i])
            if graph[nby][nbx] != 'O':
                if graph[nry][nrx] == 'O':
                    print(depth)
                    return
                if nry == nby and nrx == nbx:
                    if rcnt < bcnt:
                        nbx -= dx[i]
                        nby -= dy[i]
                    else:
                        nrx -= dx[i]
                        nry -= dy[i]
                if not visit[nry][nrx][nby][nbx]:
                    visit[nry][nrx][nby][nbx] = True
                    q.append((nrx, nry, nbx, nby, depth + 1))
    print(-1)

BFS()