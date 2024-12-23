import sys
from collections import deque
input = sys.stdin.readline

def solution(N: int, K: int) -> None:
    times = [False] * 100001
    counts = [0] * 100001
    q = deque()

    q.append((N, 0))
    flag = True
    while q:
        now, time = q.popleft()
        if now == K:
            flag = False
        if not times[now] or times[now] >= time:
            times[now] = time
            counts[now] += 1
            if flag:
                if now - 1 >= 0:
                    q.append((now - 1, time + 1))
                if now + 1 < 100001:
                    q.append((now + 1, time + 1))
                if now * 2 < 100001:
                    q.append((now * 2, time + 1))

    print(times[K])
    print(counts[K])

N, K = map(int, input().split())
solution(N, K)