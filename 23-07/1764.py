import sys
read = sys.stdin.readline

dj = set()
bj = set()
answers = []

N, M = map(int, read().split())
for _ in range(N):
    dj.add(read())
for _ in range(M):
    bj.add(read())

answers = sorted(list(dj & bj))

print(len(answers))
for answer in answers:
    print(answer, end="")