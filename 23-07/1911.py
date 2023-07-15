import sys
read = sys.stdin.readline

pool = []
answer = 0

N, L = map(int, read().split())

for _ in range(N):
    poolStart, poolEnd = map(int, read().split())
    pool.append([poolStart, poolEnd])

pool.sort(key=lambda x:x[0])

plank = pool[0][0]
for left, right in pool:
    if plank > right:
        continue
    if plank < left:
        plank = left
    count = (right - plank) // L
    if (right - plank) % L:
        count += 1

    plank += count * L
    answer += count
    print("=>", count, plank)

print(answer)