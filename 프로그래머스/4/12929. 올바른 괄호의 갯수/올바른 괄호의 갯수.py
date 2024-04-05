def solution(n):
    DP = [1] + [0] * n
    for i in range(1, n + 1):
        for j in range(i):
            DP[i] += DP[i - j - 1] * DP[j]
    
    return DP[n]