import sys
from collections import deque
input = sys.stdin.readline

def solution(M, N, maze):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    board = [[-1] * M for _ in range(N)]
    q = deque()
    q.append((0, 0))
    board[0][0] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if board[ny][nx] < 0:
                if maze[ny][nx] == "1":
                    board[ny][nx] = board[y][x] + 1
                    q.append((nx, ny))
                else:
                    board[ny][nx] = board[y][x]
                    q.appendleft((nx, ny))
    print(board[N - 1][M - 1])

M, N = map(int, input().split())
maze = [list(input().strip()) for _ in range(N)]
solution(M, N, maze)