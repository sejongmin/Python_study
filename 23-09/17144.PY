import sys
read = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
cleaner = []

R, C, T = map(int, read().split())
graph = [list(map(int, read().split())) for _ in range(R)]
for i in range(R):
    if graph[i][0] == -1:
        cleaner.append(i)
        graph[i][0] = 0

def dust(board):
    new_board = [board[i][:] for i in range(R)]
    for i in range(R):
        for j in range(C):
            if board[i][j] > 4:
                now = board[i][j] // 5
                for k in range(4):
                    ny, nx = i + dy[k], j + dx[k]
                    if nx < 0 or nx >= C or ny < 0 or ny >= R:
                        continue
                    if nx == 0 and ny in cleaner:
                        continue
                    new_board[i][j] -= now
                    new_board[ny][nx] += now
    return new_board

def clean(board):
    new_board = [board[i][:] for i in range(R)]

    #위 반시계 방향
    for i in range(cleaner[0] - 1, 0, -1):
        new_board[i][0] = new_board[i - 1][0]
    new_board[0].pop(0)
    new_board[0].append(new_board[1][C - 1])
    for i in range(1, cleaner[0]):
        new_board[i][C - 1] = new_board[i + 1][C - 1]
    new_board[cleaner[0]].insert(0, 0)
    new_board[cleaner[0]].pop(C)
    #아래 시계 방향
    for i in range(cleaner[1] + 1, R - 1):
        new_board[i][0] = new_board[i + 1][0]
    new_board[R - 1].pop(0)
    new_board[R - 1].append(new_board[R - 2][C - 1])
    for i in range(R - 2, cleaner[1], -1):
        new_board[i][C - 1] = new_board[i - 1][C - 1]
    new_board[cleaner[1]].insert(0, 0)
    new_board[cleaner[1]].pop(C)

    return new_board



board = [graph[i] for i in range(R)]
for i in range(T):
    board = dust(board)
    board = clean(board)

answer = 0
for i in range(R):
    answer += sum(board[i])
print(answer)