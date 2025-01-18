import sys
input = sys.stdin.readline

def solution(N: int, S: int, arr: list) -> int:
    answer = 100001
    acc_sum = [0] * (N + 1)
    for i in range(1, N + 1):
        acc_sum[i] = acc_sum[i - 1] + arr[i - 1]
    
    front, rear = 0, 0
    while rear <= N:
        sub_sum = acc_sum[rear] - acc_sum[front]
        if sub_sum >= S:
            answer = min(answer, rear - front)
            if answer == 1:
                break
            front += 1
        elif sub_sum < S:
            rear += 1
        
    return answer if answer != 100001 else 0

N, S = map(int, input().split())
arr = list(map(int, input().split()))
print(solution(N, S, arr))