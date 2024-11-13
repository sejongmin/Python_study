import sys
from collections import deque
input = sys.stdin.readline

def solution(N, nodes):
    parents = [0] * (N + 1)
    q = deque()
    q.append(1)
    while q:
        p = q.popleft()
        for node in nodes[p]:
            if not parents[node]:
                parents[node] = p
                q.append(node)
    
    for i in range(2, N + 1):
        print(parents[i])

N = int(input())
nodes = {i: [] for i in range(1, N + 1)}
for i in range(N - 1):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)
solution(N, nodes)