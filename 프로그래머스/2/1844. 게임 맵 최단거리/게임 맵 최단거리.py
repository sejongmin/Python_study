from collections import deque

def solution(maps):
    def dfs(maps):
        r, c = 0, 0
        dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
        queue = deque([(0, 0, 1)])
        visited = set([(0, 0)])
        n, m = len(maps) - 1, len(maps[0]) - 1
        
        while queue:
            r, c, dist = queue.popleft()
            if r == n and c == m:
                return dist
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if (nr, nc) in visited:
                    continue
                if nr < 0 or nr > n or nc < 0 or nc > m or maps[nr][nc] == 0:
                    continue
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))
        return -1
    return dfs(maps)