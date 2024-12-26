import sys
input = sys.stdin.readline

def solution(N: int, A : list) -> None:
    increase = [1] * N
    decrease = [1] * N
    for i in range(N):
        for j in range(i):
            if A[i] > A[j]:
                increase[i] = max(increase[i], increase[j] + 1)
            if A[N-i-1]  > A[N-1-j]:
                decrease[N-i-1] = max(decrease[N-i-1], decrease[N-1-j] + 1)
    answer = 0
    for i in range(N):
        answer = max(answer, increase[i] + decrease[i] - 1)
    
    print(answer)

N = int(input())
A = list(map(int, input().split()))
solution(N, A)