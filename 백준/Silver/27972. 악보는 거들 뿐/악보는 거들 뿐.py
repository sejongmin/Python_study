import sys
input = sys.stdin.readline

def solution(M, P):
    answer = 0
    up, down = 0, 0
    for i in range(1, M):
        if P[i] > P[i - 1]:
            up += 1
            down = 0
        elif P[i] < P[i - 1]:
            down += 1
            up = 0
        answer = max(answer, max(up, down))
    print(answer + 1)

M = int(input())
P = list(map(int, input().split()))
solution(M, P)