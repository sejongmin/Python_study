import sys
input = sys.stdin.readline

def solution(N, cards):
    dp = [0] * (N + 1)

    for i in range(N):
        for j in range(i + 1, N + 1):
            dp[j] = max(dp[j], dp[j - i - 1] + cards[i])
    
    return dp[-1]
    

N = int(input())
cards = list(map(int, input().split()))
print(solution(N, cards))