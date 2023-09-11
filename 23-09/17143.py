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

def moveShark(board):
    new_board = [[[False, 0, 0, 0] for i in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if board[i][j][0]:
                if board[i][j][2] == 1:
                    now = i - board[i][j][1]
                    if now // R % 2:
                        if new_board[now % R][j][3] < board[i][j][3]:
                            new_board[now % R][j] = [True, board[i][j][1], 2, board[i][j][3]]
                    else:
                        if new_board[R - 1 - (now % R)][j][3] < board[i][j][3]:
                            new_board[R - 1 - (now % R)][j] = [True, board[i][j][1], 1, board[i][j][3]]
                elif board[i][j][2] == 2:
                    now = i + board[i][j][1]
                    if now // R % 2:
                        if new_board[R - 1 - ((now + 1) % R)][j][3] < board[i][j][3]:
                            new_board[R - 1 - ((now + 1) % R)][j] = [True, board[i][j][1], 1, board[i][j][3]]
                    else:
                        if new_board[now % R][j][3] < board[i][j][3]:
                            new_board[now % R][j] = [True, board[i][j][1], 2, board[i][j][3]]

                elif board[i][j][2] == 3:
                    now = j + board[i][j][1]
                    if now // C % 2:
                        if new_board[i][C - 1 - ((now + 1) % C)][3] < board[i][j][3]:
                            new_board[i][C - 1 - ((now + 1) % C)] = [True, board[i][j][1], 4, board[i][j][3]]
                    else:
                        if new_board[i][now % C][3] < board[i][j][3]:
                            new_board[i][now % C] = [True, board[i][j][1], 3, board[i][j][3]]
                else:
                    now = j - board[i][j][1]
                    if now // C % 2:
                        if new_board[i][abs(now) % C][3] < board[i][j][3]:
                            new_board[i][abs(now) % C] = [True, board[i][j][1], 3, board[i][j][3]]
                    else:
                        if new_board[i][C - 1 - (now % C)][3] < board[i][j][3]:
                            new_board[i][C - 1 - (now % C)] = [True, board[i][j][1], 4, board[i][j][3]]
    return new_board

for i in range(C):
    board = getShark(board, i)
    board = moveShark(board)

print(answer)