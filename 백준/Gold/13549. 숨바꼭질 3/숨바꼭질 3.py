import sys
from collections import deque
input = sys.stdin.readline

def solution(N, K):
    INF = 100001
    q = deque()
    q.append(N)
    time = [-1] * INF
    time[N] = 0
    while q:
        pos = q.popleft()
        if pos == K:
            return time[pos]
        if pos * 2 < INF and time[pos * 2] == -1:
            time[pos * 2] = time[pos]
            q.append(pos * 2)
        if pos - 1 >= 0 and time[pos - 1] == -1:
            time[pos - 1] = time[pos] + 1
            q.append(pos - 1)
        if pos + 1 < INF and time[pos + 1] == -1:
            time[pos + 1] = time[pos] + 1
            q.append(pos + 1)

N, K = map(int, input().split())
print(solution(N, K))