M, N, B = map(int, input().split())
ground = []
for i in range(M):
    ground += list(map(int, input().split()))

min_time = 500*500*2*256
answer = 0

for target in range(max(ground), min(ground) - 1, -1):
    if sum(ground) + B < M * N * target:
        continue

    time = 0
    for i in ground:
        if i > target:
            time += (i - target) * 2
        else:
            time += (target - i)
    
    if (min_time > time):
        min_time = time
        answer = target

print(min_time, answer)