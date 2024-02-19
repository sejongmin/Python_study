def solution(board):
    answer = 0
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    q = []
    
    for i in range(len(board)):
        board[i] = list(board[i])
        if 'R' in board[i]:
            q.append((i, board[i].index('R'), 0))
    
    w, h = len(board[0]), len(board)
    visit = [[False] * w for _ in range(h)]
    visit[q[0][0]][q[0][1]] = True
    
    while q:
        y, x, depth = q.pop(0)
        for k in range(4):
            ny, nx = y, x
            while True:
                ny, nx = ny + dy[k], nx + dx[k]
                if ny < 0 or nx < 0 or ny >= h or nx >= w or board[ny][nx] == 'D':
                    ny, nx = ny - dy[k], nx - dx[k]
                    break
            if visit[ny][nx]:
                continue
            if board[ny][nx] == 'G':
                return depth + 1
            visit[ny][nx] = True
            q.append((ny, nx, depth + 1))
            
    return -1