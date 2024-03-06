import heapq

def find(x, roots):
    if x != roots[x]:
        r = find(roots[x], roots)
        roots[x] = r
        return r
    return x

def union(x, y, roots):
    x_root = find(x, roots)
    y_root = find(y, roots)
    if x_root < y_root:
        roots[y_root] = x_root
    else:
        roots[x_root] = y_root


def solution(land, height):
    answer = 0
    N = len(land)
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    visit = [[False] * N for _ in range(N)]
    graph = [[0] * N for _ in range(N)]
    hq = []
    number = 0
    
    for i in range(N):
        for j in range(N):
            if visit[i][j]:
                continue
            number += 1
            q = [(i, j)]
            visit[i][j] = True
            graph[i][j] = number
            while q:
                y, x = q.pop(0)
                for k in range(4):
                    ny, nx = y + dy[k], x + dx[k]
                    if nx < 0 or ny < 0 or nx >= N or ny >= N:
                        continue
                    cost = abs(land[y][x] - land[ny][nx])
                    if visit[ny][nx] or cost > height:
                        if visit[ny][nx] and cost > height and number != graph[ny][nx]:
                            heapq.heappush(hq, (cost, number, graph[ny][nx]))
                        continue
                    q.append((ny, nx))
                    visit[ny][nx] = True
                    graph[ny][nx] = number

    roots = [i for i in range(number)]
    while hq:
        weight, node1, node2 = heapq.heappop(hq)
        if find(node1 - 1, roots) != find(node2 - 1, roots):
            answer += weight
            union(node1 - 1, node2 - 1, roots)
            
    return answer