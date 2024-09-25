import sys
input = sys.stdin.readline

answer = 0
N = int(input())
for i in range(N):
    p, a = map(int, input().split())
    answer += a % p
print(answer)