import sys
input = sys.stdin.readline

def solution(N):
    NUM_RANGE = 10
    BIT_RANGE = 1 << NUM_RANGE
    MOD = int(10e8)

    if N < 10:
        return 0
    
    dp = [[[0] * BIT_RANGE for j in range(NUM_RANGE)] for i in range(N)]
    for k in range(NUM_RANGE):
        dp[0][k][1 << k] = 1

    for i in range(1, N):
        for j in range(NUM_RANGE):
            for b in range(BIT_RANGE):
                if j > 0:
                    dp[i][j][b | 1 << j] += dp[i - 1][j - 1][b]
                if j < 9:
                    dp[i][j][b | 1 << j] += dp[i - 1][j + 1][b]

    total = 0
    for i in range(1, NUM_RANGE):
        total += dp[N - 1][i][0b1111111111]

    return total % MOD

N = int(input())
print(solution(N))
