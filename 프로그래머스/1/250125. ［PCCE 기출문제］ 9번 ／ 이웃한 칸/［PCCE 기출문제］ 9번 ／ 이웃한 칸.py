def solution(board, h, w):
    answer = 0
    select = board[h][w]
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    for i in range(4):
        nh, nw = h + dy[i], w + dx[i]
        if nh < 0 or nw < 0 or nh >= len(board) or nw >= len(board):
            continue
        if select == board[nh][nw]:
            answer += 1
    return answer