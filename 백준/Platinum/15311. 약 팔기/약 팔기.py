import sys
input = sys.stdin.readline

def solution(k: int) -> None:
    print(2000)
    print(*(1 for _ in range(1000)), *(1000 for _ in range(1000)))

K = int(input())
solution(K)