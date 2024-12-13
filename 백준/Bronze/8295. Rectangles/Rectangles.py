import sys
input = sys.stdin.readline

def solution(n: int, m: int, p: int):
    answer = 0
    for row in range(1, n + 1):
        for col in range(1, m + 1):
            perimeter = 2 * (row + col)
            if p > perimeter:
                continue
            answer += (n + 1 - row) * (m + 1 - col)

    print(answer)
n, m, p = map(int, input().split())
solution(n, m, p)