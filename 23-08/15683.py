import sys
read = sys.stdin.readline

cctv = []
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 64

N, M = map(int, read().split())
for i in range(N):
    line = list(map(int, read().split()))
    for j in range(M):
        if line[j] != 0 and line[j]!= 6:
            cctv.append([line[j], i, j])
    graph.append(line)

def DFS(board, depth):
    if depth == len(cctv):
        global answer
        cnt = 0
        for i in range(N):
            cnt += board[i].count(0)
        answer = min(answer, cnt)
        return
    
    c = cctv[depth]
    if c[0] == 1:
        for i in range(4):
            board_copy = [[a for a in board[b]] for b in range(N)]
            x, y = c[2], c[1]
            nx = x + dx[i]
            ny = y + dy[i]
            while nx >= 0 and nx < M and ny >= 0 and ny < N:
                if board_copy[ny][nx] == 6:
                    break
                if board_copy[ny][nx] == 0:
                    board_copy[ny][nx] = '#'
                nx += dx[i]
                ny += dy[i]
            DFS(board_copy, depth + 1)

    elif c[0] == 2:
        for i in range(2):
            board_copy = [[a for a in board[b]] for b in range(N)]
            x, y = c[2], c[1]
            nxA = x + dx[i * 2]
            nxB = x + dx[i * 2 + 1]
            nyA = y + dy[i * 2]
            nyB = y + dy[i * 2 + 1]
            while nxA >= 0 and nxA < M and nyA >= 0 and nyA < N:
                if board_copy[nyA][nxA] == 6:
                    break
                if board_copy[nyA][nxA] == 0:
                    board_copy[nyA][nxA] = '#'
                nxA += dx[i * 2]
                nyA += dy[i * 2]
            while nxB >= 0 and nxB < M and nyB >= 0 and nyB < N:
                if board_copy[nyB][nxB] == 6:
                    break
                if board_copy[nyB][nxB] == 0:
                    board_copy[nyB][nxB] = '#'
                nxB += dx[i * 2 + 1]
                nyB += dy[i * 2 + 1]
            DFS(board_copy, depth + 1)

    elif c[0] == 3:
        for i in range(2):
            for j in range(2):
                board_copy = [[a for a in board[b]] for b in range(N)]
                x, y = c[2], c[1]
                nx = x + dx[i]
                ny = y + dy[j + 2]
                while nx >= 0 and nx < M:
                    if board_copy[y][nx] == 6:
                        break
                    if board_copy[y][nx] == 0:
                        board_copy[y][nx] = '#'
                    nx += dx[i]
                while ny >= 0 and ny < N:
                    if board_copy[ny][x] == 6:
                        break
                    if board_copy[ny][x] == 0:
                        board_copy[ny][x] = '#'
                DFS(board_copy, depth + 1)

    elif c[0] == 4:
        for i in range(4):
            board_copy = [[a for a in board[b]] for b in range(N)]
            x, y = c[2], c[1]
            for j in range(4):
                if i == j:
                    continue
                nx = x + dx[j]
                ny = y + dy[j]
                while nx >= 0 and nx < M and ny >= 0 and ny < N:
                    if board_copy[ny][nx] == 6:
                        break
                    if board_copy[ny][nx] == 0:
                        board_copy[ny][nx] = '#'
                    nx += dx[j]
                    ny += dy[j]
            DFS(board_copy, depth + 1)

    elif c[0] == 5:
        board_copy = [[a for a in board[b]] for b in range(N)]
        x, y = c[2], c[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            while nx >= 0 and nx < M and ny >= 0 and ny < N:
                if board_copy[ny][nx] == 6:
                    break
                if board_copy[ny][nx] == 0:
                    board_copy[ny][nx] = '#'
                nx += dx[i]
                ny += dy[i]
        DFS(board_copy, depth + 1)

DFS(graph, 0)
print(answer)