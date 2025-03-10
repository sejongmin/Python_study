import sys
input = sys.stdin.readline

def solution(N, M):
    def back(now, arr):
        if now == M:
            print(*arr)
        
        for i in range(1, N + 1):
            if i not in arr:
                arr.append(i)
                back(now + 1, arr)
                arr.pop()
    back(0, [])

N, M = map(int, input().split())
solution(N, M)