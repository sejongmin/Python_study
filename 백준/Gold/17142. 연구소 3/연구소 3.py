import sys
from collections import deque
input = sys.stdin.readline

def solution(N, M, board):
    answer = int(1e9)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    space = 0
    virus = []
    for i in range(N):
        for j in range(N):
            if board[i][j] != 1:
                space += 1
            if board[i][j] == 2:
                virus.append((i, j))

    def dfs(depth, idx, vq):
        nonlocal answer
        
        if depth == M:
            cnt = len(virus)
            if cnt == space:
                answer = 0
                return
            q = deque()
            visited = set()
            for r, c in vq:
                q.append((r, c, 0))
                visited.add((r, c))
            while q:
                r, c, h = q.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if nr < 0 or nr >= N or nc < 0 or nc >= N or (nr, nc) in visited:
                        continue
                    if board[nr][nc] != 1:
                        q.append((nr, nc, h + 1))
                        visited.add((nr, nc))
                        if board[nr][nc] == 0:
                            cnt += 1
                            if cnt == space:
                                answer = min(answer, h + 1)
                                return
            return
        for i in range(idx, len(virus)):
            r, c = virus[i]
            vq.append((r, c))
            dfs(depth + 1, i + 1, vq)
            vq.pop()

    dfs(0, 0, deque())
    return answer if answer != int(1e9) else -1

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, M, board))