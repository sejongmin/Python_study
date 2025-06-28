import sys
input = sys.stdin.readline

def solution(N, M, arr, K, queries):
    answer = []
    acc = [[0] * M for _ in range(N)]

    for i in range(N):
        acc[i][0] = arr[i][0]
        for j in range(1, M):
            acc[i][j] = acc[i][j - 1] + arr[i][j]
    
    for query in queries:
        r1, c1, r2, c2 = map(lambda x: x - 1, query)
        s = 0
        for i in range(r1, r2 + 1):
            if c1 == 0:
                s += acc[i][c2]
            else:
                s += acc[i][c2] - acc[i][c1 - 1]
        
        answer.append(s)

    print(*answer, sep='\n')

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
K = int(input())
queries = [list(map(int, input().split())) for _ in range(K)]
solution(N, M, arr, K, queries)