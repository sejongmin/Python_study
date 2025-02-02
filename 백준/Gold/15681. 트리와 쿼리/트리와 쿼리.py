import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(int(10e6))

def solution(N, R, Q, edges, u):
    dp = [1] * (N + 1)
    tree = {i: [] for i in range(1, N + 1)}
    for edge in edges:
        tree[edge[0]].append(edge[1])
        tree[edge[1]].append(edge[0])
    
    def dfs(node, parent):
        for neighbor in tree[node]:
            if neighbor != parent:
                dfs(neighbor, node)
                dp[node] += dp[neighbor]
    dfs(R, -1)
    for i in range(Q):
        print(dp[u[i]])

N, R, Q = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(N - 1)]
us = [int(input()) for _ in range(Q)]
solution(N, R, Q, edges, us)
