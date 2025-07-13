import sys
input = sys.stdin.readline

def solution(N: int, M: int, K: int, A: list, trees: list) -> int:
    ground = [[5] * (N + 1) for _ in range(N + 1)]
    adjacent = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    tree_info = [[[] for _ in range(N + 1)] for i in range(N + 1)]
    for r, c, a in trees:
        tree_info[r][c].append(a)

    def spring():
        dead = [[0] * (N + 1) for _ in range(N + 1)]
        for r in range(1, N + 1):
            for c in range(1, N + 1):
                if tree_info[r][c]:
                    temp = []
                    food = ground[r][c]
                    for i in range(len(tree_info[r][c]) - 1, -1, -1):
                        tree = tree_info[r][c][i]
                        if food >= tree:
                            food -= tree
                            temp.append(tree + 1)
                        elif food < tree:
                            dead[r][c] += tree // 2
                    tree_info[r][c] = temp[::-1]
                    ground[r][c] = food
        return dead

    def summer(dead):
        for r in range(1, N + 1):
            for c in range(1, N + 1):
                ground[r][c] += dead[r][c]

    def fall():
        for r in range(1, N + 1):
            for c in range(1, N + 1):
                for tree in tree_info[r][c]:
                    if tree % 5 != 0:
                        continue
                    for dr, dc in adjacent:
                        nr, nc = r + dr, c + dc
                        if nr < 1 or nr > N or nc < 1 or nc > N:
                            continue
                        tree_info[nr][nc].append(1)

    def winter():
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                ground[i][j] = ground[i][j] + A[i - 1][j - 1]

    answer = 0
    dead = []
    for _ in range(K):
        dead = spring()
        summer(dead)
        fall()
        winter()

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            answer += len(tree_info[i][j])

    return answer

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
trees = [list(map(int, input().split())) for _ in range(M)]
print(solution(N, M, K, A, trees))
