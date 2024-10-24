import sys
import heapq
input = sys.stdin.readline

def solution(N, M):
    INF = int(10e9)
    graph = {i:[] for i in range(1, N + 1)}
    for _ in range(M):
        s, e, w = map(int, input().split())
        graph[s].append((e, w))
    s, e = map(int, input().split())
    
    result = [INF for _ in range(N + 1)]
    q = []
    heapq.heappush(q, (0, s))
    while q:
        weight, city = heapq.heappop(q)
        if result[city] < weight:
            continue
        for bus in graph[city]:
            next_weight = weight + bus[1]
            if result[bus[0]] > next_weight:
                result[bus[0]] = next_weight
                heapq.heappush(q, (next_weight, bus[0]))
    print(result[e])

N = int(input())
M = int(input())
solution(N, M)