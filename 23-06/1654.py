N, K = map(int, input().split())
lines = []

for _ in range(N):
    line = int(input())
    lines.append(line)

max_length = 0
left, right = 1, max(lines)

while left <= right:
    mid = (left + right) // 2
    count = 0

    for line in lines:
        count += line // mid

    if count >= K:
        left = mid + 1
    else:
        right = mid - 1

print(right)