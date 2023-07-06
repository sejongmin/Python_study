import sys
read = sys.stdin.readline

graph = []
virus = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, read().split())
for _ in range(N):
    line = list(map(int, read().split()))
    while 2 in line:
        virus.append((line.index(2), _))
        line[line.index(2)] = 3
    graph.append(line)

def virusDiffusion():
    virusGraph = []
    for i in range(N):
        virusGraph.append(graph[i][:])
    q = virus[:]

    while q:
        vx, vy = q.pop(0)
        for i in range(4):
            nx, ny = vx + dx[i], vy + dy[i]
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if virusGraph[ny][nx] != 0:
                continue
            virusGraph[ny][nx] = 2
            q.append((nx, ny))
    global answer
    count = 0
    for i in range(N):
        count += virusGraph[i].count(0)
    answer = max(answer, count)

def makeWall(wallCnt):
    if wallCnt == 3:
        virusDiffusion()
        return
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                makeWall(wallCnt + 1)
                graph[i][j] = 0

answer = 0
makeWall(0)
print(answer)