import sys
input = sys.stdin.readline

def solution(N):
    status = []
    while N > 0:
        if N % 2 == 1:
            status.append(1)
        else:
            status.append(0)
        N = N // 2

    return status.count(1)

N = int(input())
print(solution(N))
