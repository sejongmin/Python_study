import sys
input = sys.stdin.readline

def solution(N: int, M: int, bytes: list, costs: list) -> int:
    if sum(bytes) == M:
        return sum(costs)
    
    total = sum(costs)
    dp = [[0] * (total + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        byte = bytes[i - 1]
        cost = costs[i - 1]
        for j in range(total + 1):
            if j < cost:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost] + byte)
    
    for i in range(total):
        if dp[-1][i] >= M:
            answer = i
            break

    return answer


N, M = map(int, input().split())
bytes = list(map(int, input().split()))
costs = list(map(int, input().split()))
print(solution(N, M, bytes, costs))
