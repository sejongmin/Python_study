import sys
import heapq
read = sys.stdin.readline

q = []
answer = 0

N, C = map(int, read().split())
M = int(read())
for _ in range(M):
    a, b, c = map(int, read().split())
    heapq.heappush(q, (b, a, c))

graph = [C] * (N + 1)

while q:
    finish, start, box = heapq.heappop(q)
    minB = C
    for i in range(start, finish):
        minB = min(minB, graph[i])
    minB = min(minB, box)
    for i in range(start, finish):
        graph[i] -= minB
    answer += minB

print(answer)