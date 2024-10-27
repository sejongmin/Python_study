import sys
import heapq
input = sys.stdin.readline
INF = int(3e5)

N, M, K, X = map(int, input().split())
graph = {i:[] for i in range(1, N + 1)}

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

q = []
heapq.heappush(q, (0, X))
dist = [INF] * (N + 1)
dist[X] = 0
while q:
    w, now = heapq.heappop(q)
    if dist[now] < w:
        continue
    for city in graph[now]:
        next_dist = dist[now] + 1
        if dist[city] < next_dist:
            continue
        dist[city] = next_dist
        heapq.heappush(q, (next_dist, city))

answer = []
for i in range(1, N + 1):
    if dist[i] == K:
        answer.append(i)
    
if answer:
    print(*answer, sep="\n")
else:
    print(-1)