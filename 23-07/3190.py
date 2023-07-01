import sys
read = sys.stdin.readline

apple = []
change_d = []
moving_q = []

N = int(read())
K = int(read())

for _ in range(K):
    x, y = map(int, read().split())
    apple.append((x, y))

L = int(read())
for _ in range(L):
    s, d = map(str, read().split())
    change_d.append((int(s), d))

direction = 0 #오른쪽, 아래, 왼쪽, 위
moving_q.append((1, 1))
time = 0
length = 0
next_d = change_d.pop(0)

while 1:
    time += 1
    x, y = moving_q[length]

    if direction == 0:
        nx = x
        ny = y + 1
    elif direction == 1:
        nx = x + 1
        ny = y
    elif direction == 2:
        nx = x
        ny = y - 1
    elif direction == 3:
        nx = x - 1
        ny = y

    if (nx < 1 or nx > N or ny < 1 or ny > N) or (nx, ny) in moving_q:
        break
    moving_q.append((nx, ny))
    if (nx, ny) in apple:
        apple.remove((nx, ny))
        length += 1
    else:
        moving_q.pop(0)

    if time == next_d[0]:
        if next_d[1] == 'L':
            direction -= 1
            if direction < 0:
                direction = 3
        elif next_d[1] == 'D':
            direction = (direction + 1) % 4

        if change_d:
            next_d = change_d.pop(0)

print(time)