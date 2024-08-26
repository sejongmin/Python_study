import sys
input = sys.stdin.readline

def solution(n):
    dp = [0] * (n + 1)
    for i in range(1, int(n ** (1/2)) + 1):
        dp[i**2] = 1
    if dp[n]:
        return 1
    
    answer = 4
    for i in range(1, int(n ** (1/2)) + 1):
        if dp[n - i ** 2]:
            return 2
        for j in range(1, int((n - i ** 2) ** (1/2)) + 1):
            if dp[n - (i ** 2) - (j ** 2)]:
                answer = 3
    return answer

n = int(input())
print(solution(n))