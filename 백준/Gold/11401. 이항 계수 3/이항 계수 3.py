import sys
input = sys.stdin.readline

MOD = int(1e9) + 7
def solution(N, K):
    def factorial(a):
        res = 1
        for i in range(a, 1, -1):
            res = (res * i) % MOD
        return res

    def power(a, b):
        if b == 0:
            return 1
        elif b == 1:
            return a
        
        res = 1
        while b > 0:
            if b % 2 == 1:
                res = (res * a) % MOD
            a = (a * a) % MOD
            b = b // 2
        
        return res
    
    print(factorial(N) * power((factorial(N - K) * factorial(K)), MOD - 2) % MOD)

N, K = map(int, input().split())
solution(N, K)