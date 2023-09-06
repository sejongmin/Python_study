import sys
read = sys.stdin.readline

N, L, R = map(int, read().split())
graph = [list(map(int, read().split())) for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def openDoor():
    doors = [[[False, False, False, False] for i in range(N)] for j in range(N)]
    Flag = False
    for i in range(N):
        for j in range(N):
            for k in range(4):
                nx = j + dx[k]
                ny = i + dy[k]
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue
                gap = abs(graph[i][j] - graph[ny][nx])
                if gap >= L and gap <= R:
                    doors[i][j][k] = True
                    Flag = True
    return doors, Flag

def move(doors):
    global graph
    visit = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if True in doors[i][j]:
                a = []
                q = []
                p = 0
                index = 0
                q.append([i, j])
                visit[i][j] = True
                while(q):
                    a.append(q.pop(0))
                    x, y = a[index][1], a[index][0]
                    p += graph[y][x]
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if doors[y][x][k] and not visit[ny][nx]:
                            q.append([ny, nx])
                            visit[ny][nx] = True
                    index += 1
                now = p // index
                for k in range(index):
                    graph[a[k][0]][a[k][1]] = now

answer = 0
while True:
    doors, Flag = openDoor()
    if not Flag:
        print(answer)
        break
    move(doors)
    answer += 1
