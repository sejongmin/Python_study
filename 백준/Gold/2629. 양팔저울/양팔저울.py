import sys
input = sys.stdin.readline

def solution(N, weights, M, beads):
    dp = [[0 for _ in range(500 * i + 1)] for i in range(N + 1)]
    answer = []

    def cal(num, weight):
        if num > N:
            return
        if dp[num][weight] == 1:
            return
        dp[num][weight] = 1

        cal(num + 1, weight + weights[num - 1])
        cal(num + 1, weight)
        cal(num + 1, abs(weight - weights[num - 1]))

    cal(0, 0)

    for bead in beads:
        if bead > 500 * N:
            answer.append('N')
        elif dp[N][bead]:
            answer.append('Y')
        else:
            answer.append('N')
    print(*answer)

N = int(input())
weights = list(map(int, input().split()))
M = int(input())
beads = list(map(int, input().split()))
solution(N, weights, M, beads)
