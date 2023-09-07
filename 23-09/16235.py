import sys
read = sys.stdin.readline

N, M, K = map(int, read().split())
graph = [list(map(int, read().split())) for _ in range(N)]
field = [[5] * N for i in range(N)]
trees = [list(map(int, read().split())) for _ in range(M)]
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

def timePasses():
    new_trees = []
    dead_trees = []
    #spring
    while trees:
        tree = trees.pop(0)
        if tree[2] > field[tree[0] - 1][tree[1] - 1]:
            dead_trees.append(tree)
        elif tree[2] <= field[tree[0] - 1][tree[1] - 1]:
            field[tree[0] - 1][tree[1] - 1] -= tree[2]
            tree[2] += 1
            new_trees.append(tree)
    #summer
    while dead_trees:
        tree = dead_trees.pop()
        field[tree[0] - 1][tree[1] - 1] += tree[2] // 2
    #fall
    l = len(new_trees)
    for i in range(l):
        if new_trees[i][2] % 5 == 0:
            x, y = new_trees[i][1] - 1, new_trees[i][0] - 1
            for j in range(8):
                nx = x + dx[j]
                ny = y + dy[j]
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue
                new_trees.append([ny + 1, nx + 1, 1])
    #winter
    for i in range(N):
        for j in range(N):
            field[i][j] += graph[i][j]
    return new_trees

for i in range(K):
    trees.sort(key=lambda x:x[2])
    trees = timePasses()
print(len(trees))