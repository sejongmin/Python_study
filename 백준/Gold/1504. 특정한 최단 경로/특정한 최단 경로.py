import sys
import heapq
input = sys.stdin.readline
INF = int(10e9)

def dijkstra(s, graph):
    dist = [INF for _ in range(N + 1)]
    dist[s] = 0
    q = []
    heapq.heappush(q, (0, s))

    while q:
        weight, node = heapq.heappop(q)
        if dist[node] < weight:
            continue
        for info in graph[node]:
            next_node = info[0]
            next_weight = weight + info[1]
            if dist[next_node] > next_weight:
                dist[next_node] = next_weight
                heapq.heappush(q, (next_weight, next_node))
    return dist

N, E = map(int, input().split())
graph = {i:[] for i in range(1, N + 1)}

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())
s_dist = dijkstra(1, graph)
v1_dist = dijkstra(v1, graph)
v2_dist = dijkstra(v2, graph)

answer = min(s_dist[v1] + v1_dist[v2] + v2_dist[N], s_dist[v2] + v2_dist[v1] + v1_dist[N])
print(answer if answer < INF else -1)