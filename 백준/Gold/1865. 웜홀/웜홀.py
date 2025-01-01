import sys
input = sys.stdin.readline

def solution(N: int, M: int, W: int, edges: list) -> None:
    INF = int(10e9)
    distance = [INF] * (N + 1)
    
    for i in range(N):
        for cur_node, next_node, time in edges:
            if distance[cur_node] + time < distance[next_node]:
                distance[next_node] = distance[cur_node] + time
                if i == N - 1:
                    print("YES")
                    return
    print("NO")
    return

TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().split())
    edges = []
    for i in range(M):
        S, E, T = map(int, input().split())
        edges.append((S, E, T))
        edges.append((E, S, T))
    for i in range(W):
        S, E, T = map(int, input().split())
        edges.append((S, E, -T))
    solution(N, M, W, edges)
