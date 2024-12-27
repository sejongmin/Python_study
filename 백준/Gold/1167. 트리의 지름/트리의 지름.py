import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def solution(V, tree):
    def dfs(now, distance):
        nonlocal dist
        for n, d in tree[now]:
            if dist[n] < 0:
                dist[n] = distance + d
                dfs(n, distance + d)
    
    dist = [-1] * (V + 1)
    dist[1] = 0
    dfs(1, 0)
    v = dist.index(max(dist))

    dist = [-1] * (V + 1)
    dist[v] = 0
    dfs(v, 0)
    print(max(dist))

V = int(input())
tree = {i: [] for i in range(1, V + 1)}
for _ in range(V):
    node = list(map(int, input().split()))[:-1]
    for i in range((len(node) - 1) // 2):
        tree[node[0]].append([node[i*2+1], node[i*2+2]])
solution(V, tree)
