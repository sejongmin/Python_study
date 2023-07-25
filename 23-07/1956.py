import sys
read = sys.stdin.readline
INF = 1e9

V, E = map(int, read().split())
graph = [[INF] * V for _ in range(V)]

for _ in range(E):
    a, b, c = map(int, read().split())
    graph[a-1][b-1] = c

for i in range(V):
    for j in range(V):
        for k in range(V):
            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

answer = INF
for i in range(V):
    answer = min(answer, graph[i][i])

if answer == INF:
    print(-1)
else:
    print(answer)