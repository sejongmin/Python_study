import sys
input = sys.stdin.readline

def solution(R, C, M, sharks):
    def move(r, c, s, d):
        nr, nc = r, c
        if d == 1:
            nr = (r - s + 1) % (2 * R - 2) - 1
            if nr // (R - 1):
                d = 2
            nr = abs(nr)
            if nr >= R:
                nr = R - nr % R - 2

        elif d == 2:
            nr = (r + s - 1) % (2 * R - 2) + 1
            if nr >= R:
                nr = R - nr % R - 2
                d = 1
        
        elif d == 3:
            nc = (c + s - 1) % (2 * C - 2) + 1
            if nc >= C:
                nc = C - nc % C - 2
                d = 4

        elif d == 4:
            
            nc = (c - s + 1) % (2 * C - 2) - 1
            if nc // (C - 1):
                d = 3
            nc = abs(nc)
            if nc >= C:
                nc = C - nc % C - 2

        return nr, nc, s, d

    def next_time(board):
        new_board = [[False] * C for _ in range(R)]
        for i in range(R):
            for j in range(C):
                if board[i][j]:
                    r, c, s, d = move(i, j, board[i][j][0], board[i][j][1])
                    z = board[i][j][2]
                    if not new_board[r][c] or new_board[r][c][2] < z:
                        new_board[r][c] = (s, d, z)
        return new_board
    
    board = [[False] * C for _ in range(R)]
    for r, c, s, d, z in sharks:
        board[r - 1][c - 1] = (s, d, z)
    answer = 0
    for i in range(C):
        for j in range(R):
            if board[j][i]:
                answer += board[j][i][2]
                board[j][i] = False
                break
        board = next_time(board)
    print(answer)

R, C, M = map(int, input().split())
sharks = []
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    sharks.append([r, c, s, d, z])
solution(R, C, M, sharks)