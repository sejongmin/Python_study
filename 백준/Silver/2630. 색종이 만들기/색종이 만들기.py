import sys
input = sys.stdin.readline

def solution(N, paper):
    visit = [[False] * N for _ in range(N)]
    white = 0
    blue = 0

    def check(x, y, s):
        nonlocal paper
        for i in range(y, y + s):
            for j in range(x, x + s):
                if paper[y][x] != paper[i][j]:
                    return False
        nonlocal visit
        for i in range(y, y + s):
            visit[i][x:x+s] = [True] * s
        return True
    
    s = N
    while s > 0:
        cnt = N // s
        for i in range(cnt):
            for j in range(cnt):
                x, y = j * s, i * s
                if not visit[y][x] and check(x, y, s):
                    if paper[y][x]:
                        blue += 1
                    else:
                        white += 1
        s = s // 2

    print(white)
    print(blue)

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
solution(N, paper)