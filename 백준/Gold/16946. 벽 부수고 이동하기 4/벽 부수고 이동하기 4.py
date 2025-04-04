import sys
from collections import deque
input = sys.stdin.readline

def solution(N, M, board):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    mem = [[[False, 0] for j in range(M)] for i in range(N)]
    answer = [[0] * M for _ in range(N)]
    id_ = 1
    for i in range(N):
        for j in range(M):
            if not mem[i][j][0] and board[i][j] == '0':
                visit = set()
                q = deque()
                q.append((i, j))
                visit.add((i, j))
                while q:
                    y, x = q.pop()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if nx < 0 or nx >= M or ny < 0 or ny >= N or (ny, nx) in visit:
                            continue
                        if board[ny][nx] == '0':
                            visit.add((ny, nx))
                            q.append((ny, nx))
                p = len(visit)
                for y, x in list(visit):
                    mem[y][x][1] = p
                    mem[y][x][0] = id_
                id_ += 1
    
    for i in range(N):
        for j in range(M):
            if board[i][j] == '1':
                ids = set()
                now = 1
                for k in range(4):
                    ny = i + dy[k]
                    nx = j + dx[k]
                    if nx < 0 or nx >= M or ny < 0 or ny >= N or mem[ny][nx][0] in ids:
                        continue
                    now += mem[ny][nx][1]
                    ids.add(mem[ny][nx][0])
                answer[i][j] = now % 10
    
    for i in range(N):
        print(*answer[i], sep="")

N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]
solution(N, M, board)
