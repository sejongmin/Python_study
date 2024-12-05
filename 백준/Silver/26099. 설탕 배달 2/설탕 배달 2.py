import sys
input = sys.stdin.readline

def solution(N: int) -> None:
    cnt = 0
    while N % 5:
        N -= 3
        cnt += 1
    print(N // 5 + cnt if N >= 0 else -1)

N = int(input())
solution(N)