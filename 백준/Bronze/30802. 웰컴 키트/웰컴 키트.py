import sys
input = sys.stdin.readline

def solution(N, Ts, T, P):
    sum_t = 0
    for i in range(6):
        sum_t += (Ts[i] - 1) // T + 1
    print(sum_t)
    print(N // P, N % P)


N = int(input())
Ts = list(map(int, input().split()))
T, P = map(int, input().split())
solution(N, Ts, T, P)