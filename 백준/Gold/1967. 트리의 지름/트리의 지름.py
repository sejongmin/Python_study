import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def solution(n):
    tree = {i:[] for i in range(1, n + 1)}
    for _ in range(n - 1):
        parent, child, weight = map(int, input().split())
        tree[parent].append((child, weight))
        tree[child].append((parent, weight))
    
    def dfs(start, now):
        for node, weight in tree[start]:
            if dist[node] < 0:
                dist[node] = now + weight
                dfs(node, now + weight)

    dist = [-1] * (n + 1)
    dist[1] = 0
    dfs(1, 0)

    start = dist.index(max(dist))
    dist = [-1] * (n + 1)
    dist[start] = 0
    dfs(start, 0)

    return max(dist)

n = int(input())
print(solution(n))