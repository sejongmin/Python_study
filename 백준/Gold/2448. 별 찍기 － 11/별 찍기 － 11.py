import sys
input = sys.stdin.readline

def solution(N: int) -> None:
    board = [[' ']*(2*N) for _ in range(N)]

    def triangle(r, c):
        nonlocal board
        for i in range(3):
            for j in range(3):
                if i < 2:
                    if i == j:
                        board[r+i][c+j] = '*'
                        board[r+i][c-j] = '*'
                elif i == 2:
                    board[r+i][c+j] = '*'
                    board[r+i][c-j] = '*'
    def dfs(n, r, c):
        if n == 3:
            return
        # 1
        triangle(r, c)
        dfs(n//2, r, c)

        # 2
        triangle(r+n//2, c+n//2)
        dfs(n//2, r+n//2, c+n//2)

        # 3
        triangle(r+n//2, c-n//2)
        dfs(n//2, r+n//2, c-n//2)
    if N == 3:
        triangle(0, 2)
    dfs(N, 0, N-1)
    for i in range(N):
        print(*board[i], sep="")

N = int(input())
solution(N)