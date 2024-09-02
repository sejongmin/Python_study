import sys
from collections import deque
input = sys.stdin.readline

def solution(n, m, graph):
    answer = [[-1 if graph[i][j] else 0 for j in range(m)] for i in range(n)]
    visited = [[False] * m for _ in range(n)]
    q = deque()
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

    for i in range(n):
        if 2 in graph[i]:
            y, x = i, graph[i].index(2)
            q.append((y, x, 0))
            visited[y][x] = True
            answer[y][x] = 0
            break
    
    while q:
        y, x, cnt = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            if visited[ny][nx]:
                continue
            if not graph[ny][nx]:
                answer[ny][nx] = 0
                visited[ny][nx] = True
                continue
            answer[ny][nx] = cnt + 1
            q.append((ny, nx, cnt + 1))
            visited[ny][nx] = True
    
    return answer

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = solution(n, m, graph)
for i in range(n):
    print(*answer[i])