import sys
input = sys.stdin.readline

def solution(A:int, B:int) -> None:
    print('yes')


T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    solution(A, B)