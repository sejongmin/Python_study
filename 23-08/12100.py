import sys
read = sys.stdin.readline

N = int(read().strip())
graph = [list(map(int, read().split())) for _ in range(N)]
answer = 0

def moveUp(n, board):
    for j in range(n):
        top = 0
        for i in range(1, n):
            if board[i][j]:
                now = board[i][j]
                board[i][j] = 0
                if board[top][j] == 0:
                    board[top][j] = now
                elif board[top][j] == now:
                    board[top][j] *= 2
                    top += 1
                else:
                    top += 1
                    board[top][j] = now
    return board

def moveDown(n, board):
    for j in range(n):
        top = n - 1
        for i in range(n - 2, -1, -1):
            if board[i][j]:
                now = board[i][j]
                board[i][j] = 0
                if board[top][j] == 0:
                    board[top][j] = now
                elif board[top][j] == now:
                    board[top][j] *= 2
                    top -= 1
                else:
                    top -= 1
                    board[top][j] = now
    return board

def moveRight(n, board):
    for i in range(n):
        top = n - 1
        for j in range(n - 2, -1, -1):
            if board[i][j]:
                now = board[i][j]
                board[i][j] = 0
                if board[i][top] == 0:
                    board[i][top] = now
                elif board[i][top] == now:
                    board[i][top] *= 2
                    top -= 1
                else:
                    top -= 1
                    board[i][top] = now
    return board

def moveLeft(n, board):
    for i in range(n):
        top = 0
        for j in range(1, n):
            if board[i][j]:
                now = board[i][j]
                board[i][j] = 0
                if board[i][top] == 0:
                    board[i][top] = now
                elif board[i][top] == now:
                    board[i][top] *= 2
                    top += 1
                else:
                    top += 1
                    board[i][top] = now
    return board

def move(n, cnt, board):
    if cnt == 4:
        global answer
        for i in range(n):
            for j in range(n):
                answer = max(answer, board[i][j])
        return
    
    for i in range(4):
        board_copy = [[i for i in board[j]] for j in range(n)]
        if i == 0:
            board_new = moveUp(n, board_copy)
            move(n, cnt + 1, board_new)
        elif i == 1:
            board_new = moveDown(n, board_copy)
            move(n, cnt + 1, board_new)
        elif i == 2:
            board_new = moveRight(n, board_copy)
            move(n, cnt + 1, board_new)
        else:
            board_new = moveLeft(n, board_copy)
            move(n, cnt + 1, board_new)

move(N, 0, graph)
print(answer)