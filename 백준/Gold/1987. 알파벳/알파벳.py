import sys
input = sys.stdin.readline

def solution(R, C, graph):
    answer = 0
    alphabet = [False] * 26
    visited = [[False] * C for _ in range(R)]
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    visited[0][0] = True
    alphabet[ord(graph[0][0]) - 65] = True

    def back(x, y, now):
        nonlocal answer
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue
            if visited[nx][ny] or alphabet[ord(graph[nx][ny]) - 65]:
                continue
            visited[nx][ny] = True
            alphabet[ord(graph[nx][ny]) - 65] = True
            answer = max(answer, now)
            back(nx, ny, now + 1)
            alphabet[ord(graph[nx][ny]) - 65] = False
            visited[nx][ny] = False

    back(0, 0, 1)
    return answer + 1

R, C = map(int, input().split())
graph = [list(input().strip()) for _ in range(R)]
print(solution(R, C, graph))