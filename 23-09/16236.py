import sys
read = sys.stdin.readline

q = []
dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]
pos = []
answer = 0

N = int(read().strip())
graph = []
for i in range(N):
    line = list(map(int, read().split()))
    if 9 in line:
        pos = [i, line.index(9)]
        line[line.index(9)] = 0
    graph.append(line)

def BFS(baby, pos):
    global answer
    eat = 0
    q = [[pos[0], pos[1], 1]]
    while q:
        distance = 0
        visit = [[False] * N for _ in range(N)]
        visit[pos[0]][pos[1]] = True
        candidate = []
        while q:
            y, x, s = q.pop(0)
            if distance and s > distance:
                break
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if nx < 0 or nx >= N or ny < 0 or ny >= N or visit[ny][nx]:
                    continue
                visit[ny][nx] = True
                if graph[ny][nx] != 0 and graph[ny][nx] < baby:
                    if not candidate:
                        distance = s
                    candidate.append([ny, nx])
                else:
                    if graph[ny][nx] > baby:
                        continue
                    else:
                        q.append([ny, nx, s + 1])
                
        if distance and candidate:
            candidate.sort(key=lambda x:(x[0], x[1]))
            ny, nx = candidate.pop(0)
            graph[ny][nx] = 0
            answer += distance
            eat += 1
            if eat == baby:
                eat = 0
                baby += 1
            pos = [ny, nx]
            q = [[pos[0], pos[1], 1]]
    return

BFS(2, pos)
print(answer)