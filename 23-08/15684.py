import sys
read = sys.stdin.readline

N, M, H = map(int, read().split())
graph = [[False] * N for _ in range(H)]
for _ in range(M):
    h, v = map(int, read().split())
    graph[h - 1][v - 1] = True
answer = 4

def ladder():
    for i in range(N):
        now = i
        for j in range(H):
            if graph[j][now]:
                now += 1
            elif now > 0 and graph[j][now - 1]:
                now -= 1
        if now != i:
            return False
    return True

def DFS(cnt, x, y):
    global answer
    if answer <= cnt:
        return
    if ladder():
        answer = min(answer, cnt)
        return
    if cnt == 3:
        return
    
    for i in range(x, H):
        if i == x:
            k = y
        else:
            k = 0
        for j in range(k, N - 1):
            if graph[i][j] == False and graph[i][j + 1] == False:
                if j > 0 and graph[i][j - 1] == False:
                    graph[i][j] = True
                    DFS(cnt + 1, i, j + 2)
                    graph[i][j] = False

DFS(0, 0, 0)
print(answer)