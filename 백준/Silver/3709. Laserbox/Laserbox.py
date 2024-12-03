import sys
input = sys.stdin.readline

def solution(n, r, turners, x, y):
    dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
    board = [[False] * n for _ in range(n)]

    for turner in turners:
        board[turner[1] - 1][turner[0] - 1] = -1

    direction = -1
    x -= 1
    y -= 1

    if x == -1:
        direction = 0
    elif y == n:
        direction = 1
    elif x == n:
        direction = 2
    elif y == -1:
        direction = 3

    while True:
        x = x + dx[direction]
        y = y + dy[direction]

        if x < 0 or x >= n or y < 0 or y >= n:
            print(x + 1, y + 1)
            return
        
        if not board[y][x]:
            board[y][x] = direction
        elif board[y][x] < 0:
            direction = (direction + 1) % 4
        elif board[y][x] != direction:
            board[y][x] = direction
        elif board[y][x] == direction:
            print(0, 0)
            return

T = int(input())
for _ in range(T):
    n, r = map(int, input().split())
    turners = [list(map(int, input().split())) for _ in range(r)]
    x, y = map(int, input().split())
    solution(n, r, turners, x, y)