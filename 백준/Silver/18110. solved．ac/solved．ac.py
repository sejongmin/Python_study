import sys
input = sys.stdin.readline

N = int(input())
levels = []
for _ in range(N):
    level = int(input())
    levels.append(level)

def solution(N, levels):
    if N < 2:
        return levels[0] if N == 1 else 0
    ex = N * 0.15 + 0.5
    ex = int(ex)
    levels.sort()
    return int(sum(levels[ex:-ex]) / (N - 2 * ex) + 0.5)

print(solution(N, levels))