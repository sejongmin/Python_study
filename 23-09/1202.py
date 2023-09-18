import sys
import heapq
read = sys.stdin.readline

N, K = map(int, read().split())
jewels = []
for i in range(N):
    heapq.heappush(jewels, list(map(int, read().split())))
bags = [int(read()) for _ in range(K)]

def steal(jewels, bags):
    bags.sort()
    answer = 0
    h = []
    for bag in bags:
        while jewels and bag >= jewels[0][0]:
            heapq.heappush(h, -jewels[0][1])
            heapq.heappop(jewels)
        if h:
            answer -= heapq.heappop(h)
    return answer

print(steal(jewels, bags))