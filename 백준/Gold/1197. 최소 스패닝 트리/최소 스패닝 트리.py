import sys
import heapq
input = sys.stdin.readline

def solution(V, E, graph):
    answer = 0
    visited = [False] * (V + 1)
    q = []
    heapq.heappush(q, (0, 1, 1))

    while q:
        cost, src, dst = heapq.heappop(q)
        if visited[dst]:
            continue
        visited[dst] = True
        answer += cost
        for node, weight in graph[dst]:
            if visited[node]:
                continue
            heapq.heappush(q, (weight, dst, node))
    print(answer)

V, E = map(int, input().split())
graph = {i: [] for i in range(1, V + 1)}
for _ in range(E):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))
solution(V, E, graph)
