import sys
from collections import deque
input = sys.stdin.readline

def solution(N, edges):
    tree = {i: [] for i in range(1, N + 1)}
    for edge in edges:
        tree[edge[0]].append(edge[1])
        tree[edge[1]].append(edge[0])

    cnt = 0
    q = deque([(1, 0)])
    visited = set()
    visited.add(1)
    while q:
        now, depth = q.popleft()
        if now != 1 and len(tree[now]) == 1:
            cnt += depth
            continue

        for node in tree[now]:
            if node not in visited:
                visited.add(node)
                q.append((node, depth + 1))

    if cnt % 2 == 0:
        print("No")
    elif cnt % 2 == 1:
        print("Yes")

N = int(input())
edges = [list(map(int, input().split())) for _ in range(N - 1)]
solution(N, edges)