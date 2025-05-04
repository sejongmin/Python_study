import sys
input = sys.stdin.readline

def solution(L, N, K, arr):
    answer = []
    for i in range(L + 1):
        now = L + 1
        for j in range(N):
            if now > abs(i - arr[j]):
                now = abs(i - arr[j])
        answer.append(now)
    print(*sorted(answer)[:K], sep='\n')

L, N, K = map(int, input().split())
arr = list(map(int, input().split()))
solution(L, N, K, arr)
