import sys
read = sys.stdin.readline

R, C = map(int, read().split())
pond = []
swan = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(R):
    ROW = list(map(str, read().strip()))
    while 'L' in ROW:
        swan.append((i, ROW.index('L')))
        ROW[ROW.index('L')] = '.'
    pond.append(ROW)

def checkPossible(x, y, R, C):
    if (x < 0 or x >= C or y < 0 or y >= R):
        return False
    return True

def meetSwan(x, y, R, C, swan):
    visit[y][x] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if checkPossible(nx, ny, R, C) and visit[ny][nx] == False:
            if pond[ny][nx] == 'X':
                visit[ny][nx] = True
                continue
            meetSwan(nx, ny, R, C, swan)

Sy, Sx = swan[0]
day = 0
yesterday = '.'

while True:
    for i in range(R):
        for j in range(C):
            if pond[i][j] != yesterday:
                continue
            for k in range(4):
                nx = j + dx[k]
                ny = i + dy[k]
                if checkPossible(nx, ny, R, C) and pond[ny][nx] == 'X':
                    pond[ny][nx] = day
    yesterday = day
    day += 1

    visit = [[False for i in range(C)] for j in range(R)]
    meetSwan(Sx, Sy, R, C, swan)
    if visit[swan[1][0]][swan[1][1]] == True:
        break

print(day)