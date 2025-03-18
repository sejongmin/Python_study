import sys
import bisect
input = sys.stdin.readline

def solution(T, n, A, m, B):
    answer = 0
    sum_A = []
    sum_B = []
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += A[j]
            sum_A.append(s)
    for i in range(m):
        s = 0
        for j in range(i, m):
            s += B[j]
            sum_B.append(s)
    
    sum_B.sort()
    for a in sum_A:
        left = bisect.bisect_left(sum_B, T - a)
        right = bisect.bisect_right(sum_B, T - a)

        answer += right - left
    return answer

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))
print(solution(T, n, A, m, B))
