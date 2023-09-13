import sys
import heapq
read = sys.stdin.readline

N = int(read().strip())
K = int(read().strip())
graph = list(map(int, read().split()))
graph.sort()

now_length = graph[-1] - graph[0]

heap = []
for i in range(N - 1):
    heapq.heappush(heap, -(graph[i + 1] - graph[i]))

for i in range(K - 1):
    if heap:
        now_length += heapq.heappop(heap)
    else:
        break

print(now_length)