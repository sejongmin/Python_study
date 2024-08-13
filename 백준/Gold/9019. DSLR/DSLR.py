import sys
from collections import deque

input = sys.stdin.readline

def solution(A, B):
    q = deque([(A, "")])
    visit = [False] * 10001

    while q:
        x, c = q.popleft()

        if x == B:
            return c
        
        cx = (x * 2) % 10000
        if not visit[cx]:
            q.append((cx, c + "D"))
            visit[cx] = True

        cx = (x - 1) % 10000
        if not visit[cx]:
            q.append((cx, c + "S"))
            visit[cx] = True

        cx = x * 10 + x // 1000 - x // 1000 * 10000
        if not visit[cx]:
            q.append((cx, c + "L"))
            visit[cx] = True

        cx = x // 10 + x % 10 * 1000
        if not visit[cx]:
            q.append((cx, c + "R"))
            visit[cx] = True

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(solution(A, B))
