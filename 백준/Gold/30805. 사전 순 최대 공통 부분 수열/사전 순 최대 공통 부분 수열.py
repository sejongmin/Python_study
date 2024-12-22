import sys
input = sys.stdin.readline

def solution(N: int, A: list, M: int, B: list) -> None:
    if commons := set(A) & set(B):
        sub = []
        while commons:
            max_val = max(commons)
            sub.append(max_val)
            A = A[A.index(max_val) + 1:]
            B = B[B.index(max_val) + 1:]
            commons = set(A) & set(B)
        print(len(sub))
        print(*sub)
    else:
        print(0)

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
solution(N, A, M, B)