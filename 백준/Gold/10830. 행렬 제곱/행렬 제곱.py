import sys
input = sys.stdin.readline

def solution(N, B, matrix):
    def dot(m1, m2):
        m = [[0] * N for _ in range(N)]

        for i in range(N):
            for j in range(N):
                for k in range(N):
                    m[i][j] += m1[i][k] * m2[k][j]
                m[i][j] %= 1000

        return m
    
    def mul(m, b):
        if b == 1:
            s = [[1 if i == j else 0 for i in range(N)] for j in range(N)]
            return dot(m, s)
        
        s = mul(m, b // 2)
        if b % 2:
            s = dot(dot(s, s), m)
        else:
            s = dot(s, s)
        
        return s

    result = mul(matrix, B)
    for i in range(N):
        print(*result[i])


N, B = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
solution(N, B, matrix)