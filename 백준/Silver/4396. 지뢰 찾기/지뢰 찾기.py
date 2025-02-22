import sys
input = sys.stdin.readline

def solution(N, board1, board2):
    dr = [-1, -1, -1, 0, 0, 1, 1, 1]
    dc = [-1, 0, 1, -1, 1, -1, 0, 1]
    mines = []
    for i in range(N):
        for j in range(N):
            if board1[i][j] == '*':
                mines.append((i, j))
    answer = [['.'] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board2[i][j] == 'x':
                now = 0
                if board1[i][j] == '.':
                    for k in range(8):
                        nr, nc = i + dr[k], j + dc[k]
                        if nr < 0 or nr >= N or nc < 0 or nc >= N:
                            continue
                        if board1[nr][nc] == '*':
                            now += 1
                    answer[i][j] = now
                else:
                    for r, c in mines:
                        answer[r][c] = '*'

    for i in range(N):
        print(*answer[i], sep="")

N = int(input())
board1 = [input().strip() for _ in range(N)]
board2 = [input().strip() for _ in range(N)]
solution(N, board1, board2)