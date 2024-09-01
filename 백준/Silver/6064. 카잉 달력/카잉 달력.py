import sys
input = sys.stdin.readline

def solution(M, N, x, y):
    for i in range(M):
        y_ = y + N * i
        x_ = y_ % M if y_ % M else M
        if x_ == x:
            return y_
    return -1

T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    print(solution(M, N, x, y))