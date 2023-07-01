import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

N, M, X = map(int, input().split())
paths = [[] for _ in range(N + 1)]

for i in range(M):
    start, finish, time = map(int, input().split())
    paths[start].append((finish, time))

def djikstra(X):
    q = []
    answer = [INF] * (N + 1)

    heapq.heappush(q, (0, X))
    answer[X] = 0

    while q:
        distance, node = heapq.heappop(q)
        
        if distance > answer[node]:
            continue

        for i, node_cost in paths[node]:
            cost = node_cost + distance

            if answer[i] > cost:
                heapq.heappush(q, (cost, i))
                answer[i] = cost

    return answer

toHome = djikstra(X)
ans = 0
for i in range(1, N + 1):
    fromHome = djikstra(i)
    ans = max(ans, fromHome[X] + toHome[i])

print(ans)