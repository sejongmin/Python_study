import sys
input = sys.stdin.readline

def solution(N, M, arr):
    answer = 0
    s = arr[0]
    front, rear = 1, 0

    while True:
        if s == M:
            answer += 1
            s -= arr[rear]
            rear += 1
        elif s < M:
            if front < N:
                s += arr[front]
                front += 1
            elif front == N:
                break
        elif s > M:
            s -= arr[rear]
            rear += 1
    
    return answer

N, M = map(int, input().split())
arr = list(map(int, input().split()))
print(solution(N, M, arr))
