import sys
from collections import deque
input = sys.stdin.readline

def solution(N, M, H):
    answer = 0
    total = N * M * H
    cnt = 0
    dx, dy, dz = [1, -1, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0], [0, 0, 0, 0, 1, -1]
    q = deque()
    boxes = []
    for i in range(H):
        boxes.append([])
        for j in range(M):
            tomatos = list(map(int, input().split()))
            boxes[i].append(tomatos)
            for k in range(N):
                if tomatos[k] == 1:
                    q.append((i, j, k, 0))
                    cnt += 1
                if tomatos[k] == -1:
                    total -= 1

    while q:
        z, y, x, day = q.popleft()
        answer = max(answer, day)
        for i in range(6):
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M or nz < 0 or nz >= H:
                continue
            if boxes[nz][ny][nx] == 0:
                cnt += 1
                q.append((nz, ny, nx, day + 1))
                boxes[nz][ny][nx] = 1
    
    return answer if total == cnt else -1

N, M, H = map(int, input().split())
print(solution(N, M, H))