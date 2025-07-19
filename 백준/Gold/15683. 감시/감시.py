import sys
input = sys.stdin.readline

def solution(N: int, M: int, office: list) -> int:
    answer = int(1e9)
    directions = {
        1: [[(0, 1)], [(1, 0)], [(-1, 0)], [(0, -1)]],
        2: [[(1, 0), (-1, 0)], [(0, 1), (0, -1)]],
        3: [[(1, 0), (0, 1)], [(0, 1), (-1, 0)], [(-1, 0), (0, -1)], [(0, -1), (1, 0)]],
        4: [[(1, 0), (-1, 0), (0, 1)], [(1, 0), (0, -1), (0, 1)], [(-1, 0), (0, -1), (1, 0)], [(-1, 0), (0, -1), (0, 1)]],
        5: [[(0, 1), (1, 0), (-1, 0), (0, -1)]]

    }
    cctv = [0]
    for i in range(N):
        for j in range(M):
            if 0 < office[i][j] < 6:
                cctv.append((i, j, office[i][j]))
            if office[i][j] == 6:
                office[i][j] = '-'
    
    def back(index):
        nonlocal answer
        if index == len(cctv):
            count = 0
            for i in range(N):
                for j in range(M):
                    if office[i][j] == 0:
                        count += 1
            answer = min(answer, count)
            return

        x, y, num = cctv[index]
        office[x][y] = index
        for direction in directions[num]:
            for dx, dy in direction:
                nx, ny = x, y
                while 1:
                    nx, ny = nx + dx, ny + dy
                    if nx < 0 or nx >= N or ny < 0 or ny >= M or office[nx][ny] == '-':
                        break
                    if office[nx][ny] == 0:
                        office[nx][ny] = index
            back(index + 1)
            for dx, dy in direction:
                nx, ny = x, y
                while 1:
                    nx, ny = nx + dx, ny + dy
                    if nx < 0 or nx >= N or ny < 0 or ny >= M or office[nx][ny] == '-':
                        break
                    if office[nx][ny] == index:
                        office[nx][ny] = 0
    back(1)
    return answer

if __name__ == "__main__":
    N, M = map(int, input().split())
    office = [list(map(int, input().split())) for _ in range(N)]
    print(solution(N, M, office))