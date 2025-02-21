import sys
input = sys.stdin.readline

def solution(N: int, numbers: list, M: int, questions: list) -> None:
    dp = [[False if i != j else True for j in range(N)] for i in range(N)]
    for i in range(N - 1):
        if numbers[i] == numbers[i + 1]:
            dp[i][i + 1] = True
    for i in range(2, N):
        for j in range(N):
            if j + i >= N:
                break
            if dp[j + 1][j + i - 1] and numbers[j] == numbers[j + i]:
                dp[j][j + i] = True

    for s, e in questions:
        print(1 if dp[s - 1][e - 1] else 0)

N = int(input())
numbers = list(map(int, input().split()))
M = int(input())
questions = [list(map(int, input().split())) for _ in range(M)]
solution(N, numbers, M, questions)
