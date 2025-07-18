import sys
input = sys.stdin.readline

MOD = int(1e9) + 7

def solution(N: int, K: int) -> int:
    def power(a, b):
        if b == 0:
            return 1
        if b == 1:
            return a

        res = 1
        while b:
            if b % 2 == 1:
                res = (res * a) % MOD
            a = (a * a) % MOD
            b = b // 2
        return res
    
    return (factorial[N] * power((factorial[N - K] * factorial[K]) % MOD, MOD - 2)) % MOD

if __name__ == "__main__":
    factorial = [1] * 4000001
    for i in range(2, 4000001):
        factorial[i] = (factorial[i - 1] * i) % MOD
    M = int(input())
    for _ in range(M):
        N, K = map(int, input().split())
        print(solution(N, K))