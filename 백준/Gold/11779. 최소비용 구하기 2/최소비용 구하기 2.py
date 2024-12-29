import sys
import heapq
input = sys.stdin.readline

def solution(n: int, m: int, bus: dict, src: int, dst: int) -> None:
    INF = int(10e9)
    costs = [INF] * (n + 1)
    prev = [[] for _ in range(n + 1)]
    hq = []
    heapq.heappush(hq, (0, src, []))
    costs[src] = 0

    while hq:
        cost, now, before = heapq.heappop(hq)
        if costs[now] < cost:
            continue
        for d, c in bus[now]:
            if costs[d] > c + cost:
                heapq.heappush(hq, (c + cost, d, before + [now]))
                costs[d] = c + cost
                prev[d] = before + [now]
    print(costs[dst])
    print(len(prev[dst]) + 1)
    print(*(prev[dst]), dst)

n = int(input())
m = int(input())
bus = {i:[] for i in range(1, n + 1)}
for i in range(m):
    s, d, c = map(int, input().split())
    bus[s].append((d, c))
src, dst = map(int, input().split())
solution(n, m, bus, src, dst)
