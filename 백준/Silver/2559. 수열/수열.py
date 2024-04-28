import sys
input = sys.stdin.readline

N, K = map(int, input().split())
t = list(map(int, input().split()))

now = sum(t[0:K])
answer = now

for i in range(N - K):
    now = now - t[i] + t[i + K]
    if answer < now:
        answer = now

print(answer)