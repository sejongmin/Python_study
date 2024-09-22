import sys
from collections import deque
input = sys.stdin.readline

def solution(N, M, board):
    answer = 0
    visited = [[False] * M for _ in range(N)]
    dy, dx = [0, 0, -1, 1], [-1, 1, 0, 0]
    q = deque()
    q.append((0, 0))
    visited[0][0] = True
    cnt = 1
    while cnt < N * M:
        answer += 1
        nq = []
        while q:
            y, x = q.popleft()
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if ny < 0 or ny >= N or nx < 0 or nx >= M:
                    continue
                if board[ny][nx] == 0 and not visited[ny][nx]:
                    q.append((ny, nx))
                    visited[ny][nx] = True
                    cnt += 1
                if board[ny][nx] != 0 and not visited[ny][nx]:
                    board[ny][nx] += 1
                    if board[ny][nx] == 3:
                        nq.append((ny, nx))
                        visited[ny][nx] = True
                        cnt += 1
        q = deque(nq)
    print(answer)
        

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
solution(N, M, board)