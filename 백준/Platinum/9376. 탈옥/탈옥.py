import sys
from collections import deque
input = sys.stdin.readline

INF = int(1e9)

def solution(h, w, jail):
    answer = INF
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    def bfs(x, y):
        q = deque([(x, y)])
        visited = [[-1] * (w + 2) for _ in range(h + 2)]
        visited[x][y] = 0
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= h + 2 or nc < 0 or nc >= w + 2:
                    continue
                if visited[nr][nc] != -1:
                    continue
                if jail[nr][nc] == '#':
                    visited[nr][nc] = visited[r][c] + 1
                    q.append((nr, nc))
                elif jail[nr][nc] != '*':
                    visited[nr][nc] = visited[r][c]
                    q.appendleft((nr, nc))
        return visited

    prisoner = []
    for i in range(h + 2):
        for j in range(w + 2):
            if jail[i][j] == '$':
                prisoner.append((i, j))

    a = bfs(0, 0)
    b = bfs(*prisoner[0])
    c = bfs(*prisoner[1])

    for i in range(h + 2):
        for j in range(w + 2):
            res = a[i][j] + b[i][j] + c[i][j]
            if jail[i][j] == '#':
                res -= 2
            if res >= 0:
                answer = min(answer, res)

    return answer

T = int(input())
for _ in range(T):
    h, w = map(int, input().split())
    jail = []
    jail.append(['.'] * (w + 2))
    for _ in range(h):
        jail.append(list('.' + input().strip() + '.'))
    jail.append(['.'] * (w + 2))
    print(solution(h, w, jail))
