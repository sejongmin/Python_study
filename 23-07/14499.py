import sys
read = sys.stdin.readline

dice = [[0] * 4, [0] * 4]
graph = []
dx = [0, 1, -1, 0, 0]
dy = [0, 0, 0, -1, 1]
answer = []

N, M, x, y, K = map(int, read().split())

for _ in range(N):
    line = list(map(int, read().split()))
    graph.append(line)
orders = list(map(int, read().split()))

while orders:
    order = orders.pop(0)
    nx = x + dx[order]
    ny = y + dy[order]
    if nx < 0 or nx >= M or ny < 0 or ny >= N:
        continue

    if order == 1:
        temp = dice[1].pop(0)
        dice[1].append(temp)
        dice[0][1] = dice[1][1]
        dice[0][3] = dice[1][3]
    elif order == 2:
        temp = dice[1].pop(3)
        dice[1].insert(0, temp)
        dice[0][1] = dice[1][1]
        dice[0][3] = dice[1][3]
    elif order == 3:
        temp = dice[0].pop(3)
        dice[0].insert(0, temp)
        dice[1][1] = dice[0][1]
        dice[1][3] = dice[0][3]
    elif order == 4:
        temp = dice[0].pop(0)
        dice[0].append(temp)
        dice[1][1] = dice[0][1]
        dice[1][3] = dice[0][3]


    if graph[ny][nx] != 0:
        dice[0][1] = graph[ny][nx]
        dice[1][1] = graph[ny][nx]
        graph[ny][nx] = 0
    else:
        graph[ny][nx] = dice[0][1]
    
    answer.append(dice[0][3])
    x = nx
    y = ny

for ans in answer:
    print(ans)