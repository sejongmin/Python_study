import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

def solution(N, S, arr):
    answer = 0
    for i in range(1, 1 << N):
        subsum = 0
        for j in range(N):
            if i & (1 << j):
                subsum += arr[j]
        if subsum == S:
            answer += 1
    return answer

print(solution(N, S, arr))