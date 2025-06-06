import sys
from collections import deque
input = sys.stdin.readline

def solution(N: int, edges: list):
    tree = {i: [] for i in range(1, N + 1)}
    dp = [[0, 0] for _ in range(N + 1)]
    parents = [0] * (N + 1)
    visited = [False] * (N + 1)
    order = []
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)

    q = deque()
    q.append(1)
    visited[1] = True
    while q:
        now = q.pop()
        order.append(now)
        for node in tree[now]:
            if not visited[node]:
                q.append(node)
                visited[node] = True
                parents[node] = now
    
    for now in reversed(order):
        dp[now][1] = 1
        
        for node in tree[now]:
            if node != parents[now]:
                dp[now][1] += min(dp[node][0], dp[node][1])
                dp[now][0] += dp[node][1]
        
    return min(dp[1])

N = int(input())
edges = [list(map(int, input().split())) for _ in range(N - 1)]
print(solution(N, edges))
