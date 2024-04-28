import sys
input = sys.stdin.readline

N = int(input())
num = int(input())

def solution(N, num):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    board = [[0] * N for _ in range(N)]

    c = 1
    now = 2
    x, y = N // 2, N // 2 - 1

    board[y + 1][x] = 1
    board[y][x] = 2

    while now < N ** 2:
        for i in range(4):
            if i == 1 or i == 3:
                c = c + 1 if c < N - 1 else c
            move = 0
            while move < c:
                x += dx[i]
                y += dy[i]
                now += 1
                move += 1
                board[y][x] = now

    for i in range(N):
        for j in range(N):
            if board[i][j] == num:
                answer = (i + 1, j + 1)
            print(board[i][j], end=" ")
        print()
    print(answer[0], answer[1])
    
solution(N, num)