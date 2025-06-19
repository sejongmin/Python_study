import sys
from collections import deque
input = sys.stdin.readline

INF = int(1e6)

def solution(N: int, board: list) -> int:
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visited = [[INF] * N for _ in range(N)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = 0
    while q:
        r, c = q.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            if board[nr][nc] == '1':
                dist = visited[r][c]
                if dist < visited[nr][nc]:
                    q.append((nr, nc))
                    visited[nr][nc] = dist
            if board[nr][nc] == '0':
                dist = visited[r][c] + 1
                if dist < visited[nr][nc]:
                    q.append((nr, nc))
                    visited[nr][nc] = dist
            
    return visited[N - 1][N - 1]

N = int(input())
board = [list(input().strip()) for _ in range(N)]
print(solution(N, board))
