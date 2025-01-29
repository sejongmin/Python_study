import sys
from collections import deque
input = sys.stdin.readline

def solution(N: int, K: int, delay: list, order: list, W: int) -> int:
    build = {i: [] for i in range(1, N + 1)}
    indegree = [0] * (N + 1)
    dp = [0] * (N + 1)

    for i in range(K):
        build[order[i][0]].append(order[i][1])
        indegree[order[i][1]] += 1

    q = deque()
    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = delay[i]
    
    while q:
        now = q.popleft()
        for b in build[now]:
            indegree[b] -= 1
            if indegree[b] == 0:
                q.append(b)
            dp[b] = max(dp[b], dp[now] + delay[b])
    
    return dp[W]

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    delay = [0] + list(map(int, input().split()))
    order = [list(map(int, input().split())) for i in range(K)]
    W = int(input())
    print(solution(N, K, delay, order, W))
