import sys
input = sys.stdin.readline
INF = int(10e9)

def solution(n: int, m: int, r: int, t: list, ground: dict) -> None:
    answer = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                ground[i][j] = min(ground[i][j], ground[i][k] + ground[k][j])
    
    for i in range(n):
        now = 0
        for j in range(n):
            if ground[i][j] <= m:
                now += t[j]
        answer = max(answer, now)
    
    print(answer)

n, m, r = map(int, input().split())
t = list(map(int, input().split()))
ground = [[INF if i != j else 0 for j in range(n)] for i in range(n)]
for _ in range(r):
    a, b, l = map(int, input().split())
    ground[a - 1][b - 1] = l
    ground[b - 1][a - 1] = l
solution(n, m, r, t, ground)
