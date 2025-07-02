import sys
input = sys.stdin.readline

INF = int(1e9)

def solution(N, A):
    answer = INF
    for d1 in range(1, N):
        for d2 in range(1, N):
            for x in range(N - d1 - d2):
                for y in range(d1, N - d2):
                    arr = [0] * 5
                    sections = [[0] * N for _ in range(N)]
                    for i in range(d1 + 1):
                        sections[x + i][y - i] = 5
                    for i in range(d2 + 1):
                        sections[x + i][y + i] = 5
                    for i in range(d2 + 1):
                        sections[x + d1 + i][y - d1 + i] = 5
                    for i in range(d1 + 1):
                        sections[x + d2 + i][y + d2 - i] = 5
                    flag = False

                    for r in range(N):
                        for c in range(N):
                            if (r == x and c == y) or (r == x + d1 + d2 and c == y - d1 + d2):
                                arr[4] += A[r][c]
                                continue
                            if sections[r][c] == 5:
                                flag = not flag
                                arr[4] += A[r][c]
                            elif flag:
                                arr[4] += A[r][c]
                                sections[r][c] = 5

                    for r in range(x + d1):
                        for c in range(y + 1):
                            if sections[r][c] == 5:
                                break
                            if sections[r][c] == 0:
                                arr[0] += A[r][c]
                                sections[r][c] = 1
                    
                    for r in range(x + d2 + 1):
                        for c in range(N - 1, y, -1):
                            if sections[r][c] == 5:
                                break
                            if sections[r][c] == 0:
                                arr[1] += A[r][c]
                                sections[r][c] = 2
                    
                    for r in range(x + d1, N):
                        for c in range(y - d1 + d2):
                            if sections[r][c] == 5:
                                break
                            if sections[r][c] == 0:
                                arr[2] += A[r][c]
                                sections[r][c] = 3
                
                    for r in range(x + d2 + 1, N):
                        for c in range(N - 1, y - d1 + d2 - 1, -1):
                            if sections[r][c] == 5:
                                break
                            if sections[r][c] == 0:
                                arr[3] += A[r][c]
                                sections[r][c] = 4
                    result = max(arr) - min(arr)
                    if answer > result:
                        answer = result
    return answer

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, A))