import sys
input = sys.stdin.readline

def solution(n, m):
    INF = int(10e9)
    cost = [[INF] * n for _ in range(n)]
    for i in range(n):
        cost[i][i] = 0

    for _ in range(m):
        a, b, c = map(int, input().split())
        cost[a - 1][b - 1] = min(cost[a - 1][b - 1], c)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if cost[i][j] > cost[i][k] + cost[k][j]:
                    cost[i][j] = cost[i][k] + cost[k][j]

    for i in range(n):
        result = [0 if cost[i][j] == INF else cost[i][j] for j in range(n)]
        print(*result)

n = int(input())
m = int(input())
solution(n, m)