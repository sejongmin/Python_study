def solution(maps):
    answer = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(len(maps)):
        maps[i] = list(maps[i])
        
    w, h = len(maps[0]), len(maps)
    visit = [[False] * w for _ in range(h)]
    
    for i in range(h):
        for j in range(w):
            if (maps[i][j] == "X" or visit[i][j]):
                continue

            score = 0
            visit[i][j] = True
            q = [(i, j)]
            while q:
                y, x = q.pop(0)
                score += int(maps[y][x])
                for k in range(4):
                    ny, nx = y + dy[k], x + dx[k]
                    if (ny < 0 or ny >= h or nx < 0 or nx >= w):
                        continue
                    if (visit[ny][nx] or maps[ny][nx] == "X"):
                        continue
                    visit[ny][nx] = True
                    q.append((ny, nx))
            answer.append(score)
            
    return sorted(answer) if len(answer) else [-1]