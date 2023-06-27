import sys
import heapq

input = sys.stdin.readline
N = int(input())
q = []
count = 0

for _ in range(N):
    s, f = map(int, input().split())
    heapq.heappush(q, (f, s))

finish, start = heapq.heappop(q)
count += 1

while q:
    next_finish, next_start = heapq.heappop(q)

    if finish > next_start:
        continue

    count += 1
    finish = next_finish
    start = next_start

print(count)