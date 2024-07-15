from collections import deque

def solution(land):
    answer = 0
    h, w = len(land), len(land[0])
    oil_dict = {0: 0}
    oil_list = [[0 for i in range(w)] for j in range(h)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    index = 1
    q = deque()
    
    for i in range(h):
        for j in range(w):
            if land[i][j] == 1 and oil_list[i][j] == 0:
                q.append((i, j))
                oil_list[i][j] = index
                oil_dict[index] = 1
                while q:
                    y, x = q.popleft()
                    for k in range(4):
                        ny, nx = y + dy[k], x + dx[k]
                        if 0 <= ny < h and 0 <= nx < w: 
                            if land[ny][nx] == 1 and oil_list[ny][nx] == 0:
                                oil_list[ny][nx] = index
                                q.append((ny, nx))
                                oil_dict[index] += 1
                index += 1
                
    for i in range(w):
        s = set()
        total = 0
        for j in range(h):
            s.add(oil_list[j][i])
        while s:
            k = s.pop()
            total += oil_dict[k]
        answer = max(answer, total)
        
    return answer