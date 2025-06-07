import sys
input = sys.stdin.readline

def solution(C, N, costs):
    INF = int(1e9)
    answer = INF
    dp = [INF] * (C + 100)
    dp[0] = 0

    for cost, customer in costs:
        for i in range(customer, C + 100):
            if dp[i] > dp[i - customer] + cost:
                dp[i] = dp[i - customer] + cost
    
    for i in range(C, C + 100):
        if answer > dp[i]:
            answer = dp[i]

    return answer

C, N = map(int, input().split())
costs = [list(map(int, input().split())) for _ in range(N)]
print(solution(C, N, costs))