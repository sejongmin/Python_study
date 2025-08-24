import sys
input = sys.stdin.readline

def solution(T: int, N: int) -> None:
    dp = [1] * 10001

    for i in range(2, 10001):
        dp[i] += dp[i - 2]

    for i in range(3, 10001):
        dp[i] += dp[i - 3]

    for i in range(T):
        print(dp[N[i]])
        
if __name__ == "__main__":
    T = int(input())
    N = [int(input()) for _ in range(T)]
    solution(T, N)
