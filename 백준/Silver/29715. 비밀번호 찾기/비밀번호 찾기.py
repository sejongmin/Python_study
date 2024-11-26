import sys
input = sys.stdin.readline

def solution(N, M, X, Y, info):
    def factorial(x):
        result = 1
        for i in range(2, x + 1):
            result *= i
        return result
    
    fixed_length = len(list(filter(lambda x:x[0] > 0, info)))

    count = factorial(N - fixed_length) // factorial(N - M)
    for i in range(N - M):
        count = count * (9 - M - i)

    print(count * X + ((count - 1) // 3) * Y)

N, M = map(int, input().split())
X, Y = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(M)]
solution(N, M, X, Y, info)