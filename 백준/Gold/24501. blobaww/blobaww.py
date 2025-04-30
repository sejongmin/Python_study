import sys
input = sys.stdin.readline

def solution(N, M, ESM):
    MOD = int(1e9) + 7
    arr_e = [[0] * M for _ in range(N)]
    arr_s = [[0] * M for _ in range(N)]
    arr_m = [[0] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if i > 0 and j == 0:
                arr_e[i][j] = arr_e[i-1][j]
            elif i == 0 and j > 0:
                arr_e[i][j] = arr_e[i][j-1]
            elif i > 0 and j > 0:
                arr_e[i][j] = arr_e[i-1][j] + arr_e[i][j-1] - arr_e[i-1][j-1]
            if ESM[i][j] == 'E':
                arr_e[i][j] += 1
    
    for i in range(N):
        for j in range(M):
            if i > 0 and j == 0:
                arr_s[i][j] = arr_s[i-1][j]
            elif i == 0 and j > 0:
                arr_s[i][j] = arr_s[i][j-1]
            elif i > 0 and j > 0:
                arr_s[i][j] = arr_s[i-1][j] + arr_s[i][j-1] - arr_s[i-1][j-1]
            if ESM[i][j] == 'S':
                arr_s[i][j] += arr_e[i][j]
    
    for i in range(N):
        for j in range(M):
            if i > 0 and j == 0:
                arr_m[i][j] = arr_m[i-1][j]
            elif i == 0 and j > 0:
                arr_m[i][j] = arr_m[i][j-1]
            elif i > 0 and j > 0:
                arr_m[i][j] = arr_m[i-1][j] + arr_m[i][j-1] - arr_m[i-1][j-1]
            if ESM[i][j] == 'M':
                arr_m[i][j] += arr_s[i][j]
    
    return arr_m[N - 1][M - 1] % MOD

N, M = map(int, input().split())
ESM = [list(input().strip()) for _ in range(N)]
print(solution(N, M, ESM))
