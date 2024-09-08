import sys
input = sys.stdin.readline

def solution(N, M, heights):
    answer = 0
    order = [[False] * N for _ in range(N)]

    for a, b in heights:
        order[a - 1][b - 1] = True

    for i in range(N):
        for j in range(N):
            for k in range(N):
                if order[j][i] and order[i][k]:
                    order[j][k] = True
    
    for i in range(N):
        cnt = 0
        for j in range(N):
            if order[i][j] or order[j][i]:
                cnt += 1
        if cnt == N - 1:
            answer += 1

    return answer

N, M = map(int, input().split())
heights = [list(map(int, input().split())) for _ in range(M)]
print(solution(N, M, heights))