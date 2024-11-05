import sys
input = sys.stdin.readline

def solution(N, M):
    def factorial(k):
        num = 1
        for i in range(1, k + 1):
            num *= i
        return num
    
    answer = factorial(M) // (factorial(N) * factorial(M - N))
    print(answer)

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    solution(N, M)