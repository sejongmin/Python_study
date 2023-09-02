import sys
read = sys.stdin.readline

N, M = map(int, read().split())
chs = []
homes = []
for i in range(N):
    line = list(map(int, read().split()))
    while 2 in line:
        ch = line.index(2)
        chs.append((i, ch))
        line[ch] = 0
    while 1 in line:
        home = line.index(1)
        homes.append((i, home))
        line[home] = 0

def DFS(cnt, index, arr):
    if cnt == M:
        global answer
        now = 0
        for hy, hx in homes:
            dist = int(10e4)
            for cy, cx in arr:
                dist = min(abs(hy - cy) + abs(hx - cx), dist)
            now += dist
        answer = min(answer, now)
        return
    
    for i in range(index + 1, len(chs)):
        arr.insert(0, chs[i])
        DFS(cnt + 1, i, arr)
        arr.pop(0)

arr = []
answer = int(10e9)
DFS(0, -1, arr)
print(answer)