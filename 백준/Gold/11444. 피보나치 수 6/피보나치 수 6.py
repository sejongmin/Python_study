import sys
input = sys.stdin.readline

def solution(N: int) -> None:
    dp = dict()
    def fibonaci(n):
        if dp.get(n, None) != None:
            return dp[n]
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        dp[n//2] = fibonaci(n//2) % 1000000007
        if n % 2 == 0:
            dp[n//2-1] = fibonaci(n//2-1) % 1000000007
            return (2*dp[n//2-1]+dp[n//2])*dp[n//2]
        if n % 2 == 1:
            dp[n//2+1] = fibonaci(n//2+1) % 1000000007
            return dp[n//2+1] ** 2 + dp[n//2] ** 2
    
    print(fibonaci(N) % 1000000007)

N = int(input())
solution(N)