import sys
input = sys.stdin.readline

def solution(N: int) -> None:
    a = N // 5
    b = N % 5 // 3
    i = 0
    while a >= 0 and a * 5 + b * 3 != N:
        i += 1
        a -= 1
        b = (N - 5 * a) // 3

    if a < 0:
        print(-1)
    else:
        print(a + b)

N = int(input())
solution(N)