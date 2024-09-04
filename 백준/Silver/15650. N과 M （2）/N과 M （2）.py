import sys
input = sys.stdin.readline

def solution(N, M):
    def back(now, idx, length):
        nonlocal N, M

        if length == M:
            print(*now)
            return

        for i in range(idx + 1, N + 1):
            now.append(i)
            back(now, i, length + 1)
            now.pop()
        return
    back([], 0, 0)

N, M = map(int, input().split())
solution(N, M)