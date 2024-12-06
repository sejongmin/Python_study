import sys
input = sys.stdin.readline

def solution(N: int, A: list) -> None:
    KIT = sum(A) // N
    answer = 0

    for i, v in enumerate(A):
        if v < KIT:
            answer += KIT - v
            A[i + 1] -= KIT - v
        elif v > KIT:
            answer += v - KIT
            A[i + 1] += v - KIT
        
    print(answer)

N = int(input())
A = list(map(int, input().split()))
solution(N, A)