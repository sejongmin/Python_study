import sys
sys.setrecursionlimit(int(10e6))
input = sys.stdin.readline

def solution(N, M, board):
    safe_zone = 0
    idx = 1
    d = {'U': (0, -1), 'D': (0, 1), 'R': (1, 0), 'L': (-1, 0)}
    visited = [[False] * (M) for _ in range(N)]

    def dfs(r, c):
        nonlocal safe_zone
        if visited[r][c]:
            if visited[r][c] == idx:
                safe_zone += 1
            return
        visited[r][c] = idx
        dfs(r + d[board[r][c]][1], c + d[board[r][c]][0])

    for r in range(N):
        for c in range(M):
            dfs(r, c)
            idx += 1

    print(safe_zone)
    
N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]
solution(N, M, board)
