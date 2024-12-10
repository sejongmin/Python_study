import sys
from collections import deque
input = sys.stdin.readline

def solution(R: int, C: int, lake: list) -> None:
    dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
    swan = []
    next_swan = deque()
    melting_points = deque()

    for i in range(R):
        for j in range(C):
            if lake[i][j] == 'L':
                swan.append((i, j))
                lake[i][j] = '.'
                melting_points.append((i, j))
            elif lake[i][j] == '.':
                melting_points.append((i, j))

    def check_meet():
        while swan_start:
            r, c = swan_start.popleft()
            if (r, c) == swan_end:
                return True
            
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
                    if lake[nr][nc] == '.':
                        swan_start.append((nr, nc))
                    elif lake[nr][nc] == 'X':
                        next_swan.append((nr, nc))
                    visited[nr][nc] = True

        return False

    def melt(melting_points):
        new_melting_points = deque()
        for i, j in melting_points:
            for k in range(4):
                nr = i + dr[k]
                nc = j + dc[k]
                if nr < 0 or nr >= R or nc < 0 or nc >= C:
                    continue
                if lake[nr][nc] == 'X':
                    new_melting_points.append((nr, nc))
                    lake[nr][nc] = '.'
        return new_melting_points

    visited = [[False] * C for _ in range(R)]
    visited[swan[0][0]][swan[0][1]] = True
    swan_start, swan_end = deque([swan[0]]), swan[1]
    day = 0
    while True:
        if check_meet():
            break
        swan_start, next_swan = next_swan, deque()
        melting_points = melt(melting_points)
        day += 1
    
    print(day)

R, C = map(int, input().split())
lake = list(list(input().strip()) for _ in range(R))
solution(R, C, lake)