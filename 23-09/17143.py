import sys
read = sys.stdin.readline

R, C, M = map(int, read().split())
#존재여부, 속력, 방향, 크기
board = [[[False, 0, 0, 0] for i in range(C)] for _ in range(R)]
for _ in range(M):
    shark = list(map(int,read().split()))
    board[shark[0] - 1][shark[1] - 1] = [True, shark[2], shark[3], shark[4]]

answer = 0

def getShark(board, index):
    global answer
    for i in range(R):
        if board[i][index][0]:
            answer += board[i][index][3]
            board[i][index] = [False, 0, 0, 0]
            return board
    return board

def moveShark(board):
    new_board = [[[False, 0, 0, 0] for i in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if board[i][j][0]:
                if board[i][j][1] == 0:
                    new_board[i][j] = board[i][j]
                    continue
                if board[i][j][2] == 1:
                    now = i - board[i][j][1]
                    if now < 0 and ((abs(now) - 1) // (R - 1)) % 2 == 0:
                        if new_board[(abs(now) - 1) % (R - 1) + 1][j][3] < board[i][j][3]:
                            new_board[(abs(now) - 1) % (R - 1) + 1][j] = [True, board[i][j][1], 2, board[i][j][3]]
                    else:
                        if new_board[R - 2 - ((abs(now) - 1) % (R - 1))][j][3] < board[i][j][3]:
                            new_board[R - 2 - ((abs(now) - 1) % (R - 1))][j] = [True, board[i][j][1], 1, board[i][j][3]]
                elif board[i][j][2] == 2:
                    now = i + board[i][j][1]
                    if now == 0 or ((now - 1) // (R - 1)) % 2 == 0:
                        if new_board[(now - 1) % (R - 1) + 1][j][3] < board[i][j][3]:
                            new_board[(now - 1) % (R - 1) + 1][j] = [True, board[i][j][1], 2, board[i][j][3]]
                    else:
                        if new_board[R - 2 - ((now - 1) % (R - 1))][j][3] < board[i][j][3]:
                            new_board[R - 2 - ((now - 1) % (R - 1))][j] = [True, board[i][j][1], 1, board[i][j][3]]

                elif board[i][j][2] == 3:
                    now = j + board[i][j][1]
                    if now == 0 or ((now - 1) // (C - 1)) % 2 == 0:
                        if new_board[i][(now - 1) % (C - 1) + 1][3] < board[i][j][3]:
                            new_board[i][(now - 1) % (C - 1) + 1] = [True, board[i][j][1], 3, board[i][j][3]]
                    else:
                        if new_board[i][C - 2 - ((now - 1) % (C - 1))][3] < board[i][j][3]:
                            new_board[i][C - 2 - ((now - 1) % (C - 1))] = [True, board[i][j][1], 4, board[i][j][3]]
                else:
                    now = j - board[i][j][1]
                    if now < 0 and ((abs(now) - 1) // (C - 1)) % 2 == 0:
                        if new_board[i][(abs(now) - 1) % (C - 1) + 1][3] < board[i][j][3]:
                            new_board[i][(abs(now) - 1) % (C - 1) + 1] = [True, board[i][j][1], 3, board[i][j][3]]
                    else:
                        if new_board[i][(abs(now) - 1) % (C - 1) + 1][3] < board[i][j][3]:
                            new_board[i][(abs(now) - 1) % (C - 1) + 1] = [True, board[i][j][1], 4, board[i][j][3]]
    return new_board

new_board = getShark(board, 0)
for i in range(1, C):
    new_board = moveShark(new_board)
    new_board = getShark(new_board, i)
print(answer)