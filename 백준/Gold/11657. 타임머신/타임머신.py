import sys
input = sys.stdin.readline

INF = int(1e9)

def solution(N: int, M: int, buses: list):
    dist = [INF] * (N + 1)
    dist[1] = 0

    for i in range(N):
        for A, B, C in buses:
            if dist[A] != INF and dist[B] > dist[A] + C:
                dist[B] = dist[A] + C

                if i == N - 1:
                    print(-1)
                    return

    for i in range(2, N + 1):
        print(dist[i] if dist[i] != INF else -1)
    return

N, M = map(int, input().split())
buses = [list(map(int, input().split())) for _ in range(M)]
solution(N, M, buses)
