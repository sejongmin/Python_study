import sys
input = sys.stdin.readline

def solution(N, m, k):
    answer = 0

    k.sort()
    a = 0
    for ki in k:
        a += ki
        if a > N:
            break
        answer += 1
    print(answer)

N, m = map(int, input().split())
k = [int(input()) for _ in range(m)]
solution(N, m, k)
