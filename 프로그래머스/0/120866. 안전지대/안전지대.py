def solution(board):
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]
    dy = [-1, -1, -1, 0, 0, 1, 1, 1]
    answer = 0
    flag = True
    n = len(board)
    
    for y in range(n):
        for x in range(n):
            if board[y][x] == 0:
                for k in range(8):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    if board[ny][nx] == 1:
                        flag = False
                        break
                
                if flag:
                    answer += 1
                flag = True

    return answer