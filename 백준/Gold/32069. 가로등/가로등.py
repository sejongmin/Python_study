import sys
from collections import deque
input = sys.stdin.readline

def solution(L, N, K, arr):
    answer = []
    q = deque()
    visited = set()
    for i in range(N):
        visited.add(arr[i])
        q.append((arr[i], 0))

    cnt = 0
    while cnt < K:
        cnt += 1
        now, dark = q.popleft()
        if now - 1 not in visited and now > 0:
            visited.add(now - 1)
            q.append((now - 1, dark + 1))
        if now + 1 not in visited and now < L:
            visited.add(now + 1)
            q.append((now + 1, dark + 1))
        answer.append(dark)
    print(*answer, sep="\n")

L, N, K = map(int, input().split())
arr = list(map(int, input().split()))
solution(L, N, K, arr)
