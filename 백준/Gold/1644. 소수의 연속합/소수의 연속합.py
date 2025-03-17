import sys
from collections import deque
input = sys.stdin.readline

def solution(N: int) -> int:
    answer = 0
    arr = [False, False] + [True] * (N - 1)
    prime = []
    for i in range(2, N + 1):
        if arr[i]:
            prime.append(i)
            for j in range(i * 2, N + 1, i):
                arr[j] = False
    front = 0
    rear = 1
    while rear <= len(prime):
        s = sum(prime[front:rear])
        if s == N:
            answer += 1
            rear += 1
        elif s < N:
            rear += 1
        elif s > N:
            front += 1
    return answer

N = int(input())
print(solution(N))
