import sys
input = sys.stdin.readline

def solution(M: int, dices: list) -> None:
    X = 1000000007

    def cal(N, x):
        if x == 1:
            return N
        v = cal(N, x // 2)
        if x % 2 == 0:
            return v * v % X
        else:
            return v * v * N % X
    
    answer = 0
    for n, s in dices:
        k = cal(n, X - 2)
        answer = (answer + k * s % X) % X
    
    print(answer)

M = int(input())
dices = [list(map(int, input().split())) for _ in range(M)]
solution(M, dices)