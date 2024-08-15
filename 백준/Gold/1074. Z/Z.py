import sys
input = sys.stdin.readline

def solution(N, r, c):
    answer = 0
    while N > 0:
        block = 4 ** (N - 1)
        if r < 2 ** (N - 1):
            if c >= 2 ** (N - 1):
                c -= 2 ** (N - 1)
                answer += block
        else:
            r -= 2 ** (N - 1)
            if c < 2 ** (N - 1):
                answer += block * 2
            else:
                c -= 2 ** (N - 1)
                answer += block * 3
        N -= 1
    return answer

N, r, c = map(int, input().split())
print(solution(N, r, c))