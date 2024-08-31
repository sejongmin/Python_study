import sys
input = sys.stdin.readline

def solution(N, M, arr):
    INF = 5000
    answer = [INF]
    graph = [[0] + [INF] * N for _ in range(N + 1)]
    for i in range(1, N + 1):
        graph[i][i] = 0
    for a, b in arr:
        graph[a][b] = 1
        graph[b][a] = 1

    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    
    for i in range(1, N + 1):
        answer.append(sum(graph[i]))

    return answer.index(min(answer))


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
print(solution(N, M, arr))