import sys
input = sys.stdin.readline

def solution(D):
    mod = 1000000007
    mat = [
        [0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1],
        [0, 1, 0, 1, 0, 0, 1, 1],
        [0, 0, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 1, 0],
        [0, 0, 1, 1, 0, 1, 0, 1],
        [1, 1, 1, 0, 0, 0, 1, 0]
    ]
    i_mat = [[1 if i == j else 0 for j in range(8)] for i in range(8)]
    
    def multiply_matrix(mat1, mat2):
        res = [[] * 2 for _ in range(8)]
        for i in range(8):
            for j in range(8):
                now = 0
                for k in range(8):
                    now += mat1[i][k] * mat2[k][j] % mod
                res[i].append(now)
        return res
    
    while D:
        if D % 2:
            i_mat = multiply_matrix(i_mat, mat)
            D -= 1
        mat = multiply_matrix(mat, mat)
        D = D // 2

    return i_mat[0][0] % mod

D = int(input())
print(solution(D))