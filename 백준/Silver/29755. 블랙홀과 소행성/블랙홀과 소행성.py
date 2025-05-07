import sys
input = sys.stdin.readline

def solution(N, M, B, A_W):
    P = 0
    B.sort()
    for a, w in A_W:
        left = 0
        right = N - 1
        while left <= right:
            mid = (left + right) // 2
            if a < B[mid] :
                right = mid - 1
            elif a > B[mid]:
                left = mid + 1
            else:
                left = mid
                break
        now = int(1e9)
        if 0 <= right < N:
            now = min(now, abs(B[right] - a))
        if 0 <= left < N:
            now = min(now, abs(B[left] - a))
        P = max(P, w * now)
    print(P)

N, M = map(int, input().split())
B = list(map(int, input().split()))
A_W = [list(map(int, input().split())) for _ in range(M)]
solution(N, M, B, A_W)