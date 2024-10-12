import sys
from collections import deque
input = sys.stdin.readline

def solution(N, M, graph):
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    visited = [[[0] * 2 for i in range(M)] for _ in range(N)]
    q = deque([(0, 0, 0)])
    visited[0][0][0] = 1

    while q:
        x, y, b = q.popleft()
        if x == N - 1 and y == M - 1:
            return visited[N - 1][M - 1][b]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if graph[nx][ny] == 1 and b == 0:
                visited[nx][ny][1] = visited[x][y][0] + 1
                q.append((nx, ny, 1))
            if graph[nx][ny] == 0 and not visited[nx][ny][b]:
                visited[nx][ny][b] = visited[x][y][b] + 1
                q.append((nx, ny, b))
    return -1

N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]
print(solution(N, M, graph))