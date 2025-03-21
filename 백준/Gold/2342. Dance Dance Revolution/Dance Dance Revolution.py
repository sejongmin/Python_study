import sys
input = sys.stdin.readline

def solution(arr: list) -> int:
    def get_cost(now, next):
        if now == next:
            return 1
        elif now == 0:
            return 2
        elif abs(next - now) % 2 == 1:
            return 3
        elif abs(next - now) % 2 == 0:
            return 4

    INF = int(4 * 10e5)
    dp = [[[INF] * 5 for i in range(5)] for j in range(len(arr))]
    dp[0][0][0] = 0

    for i in range(len(arr) - 1):
        for r in range(5):
            for l in range(5):
                r_cost = get_cost(r, arr[i])
                l_cost = get_cost(l, arr[i])
                dp[i + 1][arr[i]][l] = min(dp[i + 1][arr[i]][l], dp[i][r][l] + r_cost)
                dp[i + 1][r][arr[i]] = min(dp[i + 1][r][arr[i]], dp[i][r][l] + l_cost)
    
    answer = INF
    for i in range(5):
        answer = min(answer, min(dp[-1][i]))
    
    return answer

arr = list(map(int, input().split()))
print(solution(arr))
