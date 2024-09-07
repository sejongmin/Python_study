import sys
input = sys.stdin.readline

def solution(N, M, aisles, K, friends):
    INF = int(10e5)
    answer = 0
    dist = INF
    rooms = [[INF if j != i else 0 for j in range(N + 1)] for i in range(N + 1)]

    for a, b, c in aisles:
        rooms[a][b] = c
        rooms[b][a] = c
    
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for k in range(1, N + 1):
                rooms[j][k] = min(rooms[j][k], rooms[j][i] + rooms[i][k])
    for i in range(1, N + 1):
        total = 0
        for friend in friends:
            total += rooms[friend][i]
        if total < dist:
            dist = total
            answer = i
    
    return answer

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    aisles = [list(map(int, input().split())) for _ in range(M)]
    K = int(input())
    friends = list(map(int, input().split()))
    print(solution(N, M, aisles, K, friends))
