import sys
read = sys.stdin.readline

board = [list(map(int, read().split())) for _ in range(5)]
arr = []
bingo = [0] * 12
for _ in range(5):
    line = list(map(int, read().split()))
    arr += line

for i in range(25):
    now = arr[i]
    for y in range(5):
        if now in board[y]:
            x = board[y].index(now)
            bingo[y] += 1
            bingo[5 + x] += 1
            if x == y:
                bingo[10] += 1
            if x == 4 - y:
                bingo[11] += 1

    if bingo.count(5) >= 3:
        print(i + 1)
        break