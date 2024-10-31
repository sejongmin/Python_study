import sys
import heapq
input = sys.stdin.readline

def solution(N, M, sight):
    INF = int(10e9)
    sight[-1] = 0
    graph = {i:[] for i in range(N)}
    for _ in range(M):
        a, b, t = map(int, input().split())
        graph[a].append((b, t))
        graph[b].append((a, t))

    q = []
    dist = [INF] * N
    dist[0] = 0
    heapq.heappush(q, (0, 0))
    while q:
        time, loc = heapq.heappop(q)
        if dist[loc] < time:
            continue
        for a in graph[loc]:
            next_loc = a[0]
            next_time = time + a[1]
            if sight[next_loc]:
                continue
            if dist[next_loc] > next_time:
                dist[next_loc] = next_time
                heapq.heappush(q, (next_time, next_loc))

    print(dist[-1] if dist[-1] < INF else -1)

N, M = map(int, input().split())
sight = list(map(int, input().split()))
solution(N, M, sight)