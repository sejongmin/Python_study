import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def solution(N: int, M: int, bridges: list, S: int, E: int) -> int:
    answer = 0
    graph = {i: [] for i in range(1, N + 1)}
    for A, B, C in bridges:
        graph[A].append((B, C))
        graph[B].append((A, C))

    dist = [0] * (N + 1)
    dist[S] = INF
    q = [(-INF, S)]

    while q:
        now_weight, now = heapq.heappop(q)
        now_weight = -now_weight
        if dist[now] > now_weight:
            continue
        for next, weight in graph[now]:
            next_weight = min(now_weight, weight)
            if dist[next] < next_weight:
                dist[next] = next_weight
                heapq.heappush(q, (-next_weight, next))

    return dist[E]

if __name__ == "__main__":
    N, M = map(int, input().split())
    bridges = [list(map(int, input().split())) for _ in range(M)]
    S, E = map(int, input().split())
    print(solution(N, M, bridges, S, E))
