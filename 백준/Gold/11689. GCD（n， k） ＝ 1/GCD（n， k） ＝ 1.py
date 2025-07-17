import sys
import math
input = sys.stdin.readline

def solution(N: int) -> int:
    x = math.ceil((N ** (1 / 2))) + 1

    is_prime = [True] * x
    for i in range(2, x):
        if not is_prime[i]:
            continue
        now = i * i
        if now < x:
            is_prime[now] = False
            now = now + i
    
    phi = 1
    for i in range(2, x):
        if not is_prime[i]:
            continue
        cnt = 0
        while N % i == 0:
            cnt += 1
            N = N // i
        if cnt == 1:
            phi = phi * (i - 1)
        elif cnt > 1:
            phi = phi * (pow(i, cnt) - int(pow(i, cnt - 1)))
    if N != 1:
        phi = phi * (N - 1)
    return phi

if __name__ == "__main__":
    N = int(input())
    print(solution(N))
    