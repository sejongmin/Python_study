import sys
input = sys.stdin.readline

def solution(arr):
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

    answer = 0
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            answer = max(answer, gcd(arr[i], arr[j]))

    print(answer)

N = int(input())
for _ in range(N):
    arr = list(map(int, input().split()))
    solution(arr)