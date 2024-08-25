import sys
from collections import deque
input = sys.stdin.readline

def solution(N, M, ladders, snakes):
    visit = [False] * 101
    q = deque([1])
    visit[1] = True
    
    cnt = 0
    while q:
        l = len(q)
        for _ in range(l):
            now = q.popleft()

            if now == 100:
                return cnt

            for i in range(1, 7):
                next_now = now + i
                if next_now <= 100 and not visit[next_now]:
                    visit[next_now] = True
                    if next_now in ladders.keys():
                        next_now = ladders[next_now]
                    elif next_now in snakes.keys():
                        next_now = snakes[next_now]
                        
                    q.append(next_now)
        cnt += 1

N, M = map(int, input().split())

ladders = {}
for _ in range(N):
    k, v = map(int, input().split())
    ladders[k] = v

snakes = {}
for _ in range(M):
    k, v = map(int, input().split())
    snakes[k] = v

print(solution(N, M, ladders, snakes))