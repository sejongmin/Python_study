import sys
from collections import deque
input = sys.stdin.readline

def solution(N, M, building, keys):
    answer = 0
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    start = []
    for i in range(N):
        if building[i][0] != '*':
            start.append((building[i][0], i, 0))
        if building[i][M-1] != '*':
            start.append((building[i][M-1], i, M-1))
    for i in range(1, M - 1):
        if building[0][i] != '*':
            start.append((building[0][i], 0, i))
        if building[N-1][i] != '*':
            start.append((building[N-1][i], N-1, i))
    
    q = deque()
    visited = set()
    keys = set(keys)
    doors = {}
    for a, i, j in start:
        if 'A' <= a <= 'Z':
            if a.lower() not in keys:
                doors[a] = doors.get(a, [])
                doors[a].append((i, j))
                continue
        elif 'a' <= a <= 'z':
            keys.add(a)
        elif a == '$':
            answer += 1

        q.append((i, j))
        visited.add((i, j))

    while q:
        y, x = q.popleft()
        for dy, dx in directions:
            ny = y + dy
            nx = x + dx
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            now = building[ny][nx]
            if (ny, nx) in visited or now == '*':
                continue
            
            if 'A' <= now <= 'Z':
                if now.lower() not in keys:
                    doors[now] = doors.get(now, [])
                    doors[now].append((ny, nx))
                    continue
            elif 'a' <= now <= 'z':
                keys.add(now)
                for i, j in doors.get(now.upper(), []):
                    q.append((i, j))
                    visited.add((i, j))
            elif now == '$':
                answer += 1
            
            q.append((ny, nx))
            visited.add((ny, nx))
    print(answer)

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    building = [list(input().strip()) for _ in range(N)]
    keys = list(input().strip())
    solution(N, M, building, keys)
