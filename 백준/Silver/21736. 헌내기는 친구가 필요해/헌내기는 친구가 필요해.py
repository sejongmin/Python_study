import sys
from collections import deque
input = sys.stdin.readline

def solution(N, M, campus):
    answer = 0
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    q = deque()
    visited = [[False] * M for _ in range(N)]
    for i in range(N):
        if 'I' in campus[i]:
            j = campus[i].index('I')
            q.append((i, j))
            visited[i][j] = True
            break
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < M :
                if visited[ny][nx] or campus[ny][nx] == 'X':
                    continue
                if campus[ny][nx] == 'P':
                    answer += 1
                q.append((ny, nx))
                visited[ny][nx] = True
    
    return answer if answer else 'TT'

N, M = map(int, input().split())
campus = [list(input().strip()) for _ in range(N)]
print(solution(N, M, campus))