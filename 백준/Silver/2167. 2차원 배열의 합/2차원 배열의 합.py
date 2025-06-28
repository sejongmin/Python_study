import sys
input = sys.stdin.readline

def solution(N, M, arr, K, queries):
    answer = []
    acc = [[0] * (M + 1) for _ in range(N + 1)]
    
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            acc[i][j] = acc[i][j - 1] + acc[i - 1][j] - acc[i - 1][j - 1] + arr[i - 1][j - 1]

    for i, j, x, y in queries:
        answer.append(acc[x][y] - acc[x][j - 1] - acc[i - 1][y] + acc[i - 1][j - 1])

    print(*answer, sep='\n')

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
K = int(input())
queries = [list(map(int, input().split())) for _ in range(K)]
solution(N, M, arr, K, queries)