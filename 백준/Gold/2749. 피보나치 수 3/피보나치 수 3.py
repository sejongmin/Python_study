import sys
input = sys.stdin.readline

MOD = int(1e6)
P = 15 * MOD // 10

def solution(N):
    N = N % P
    arr = [0, 1]
    for i in range(2, N + 1):
        arr.append((arr[i - 2] + arr[i - 1]) % MOD)
    return arr[N]

N = int(input())
print(solution(N))