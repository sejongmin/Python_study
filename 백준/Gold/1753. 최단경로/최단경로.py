import sys
import heapq
input = sys.stdin.readline

def solution(V, E, K):
    INF = 200000
    answer = [INF] * (V + 1)
    hq = []
    graph = {i:[] for i in range(1, V + 1)}
    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))

    answer[K] = 0
    heapq.heappush(hq, (0, K))
    while hq:
        weight, node = heapq.heappop(hq)
        if answer[node] < weight:
            continue
        for v, w in graph[node]:
            nw = w + weight
            if answer[v] > nw:
                answer[v] = nw
                heapq.heappush(hq, (nw, v))

    for i in range(1, V + 1):
        print(answer[i] if answer[i] < INF else "INF")

V, E = map(int, input().split())
K = int(input())
solution(V, E, K)