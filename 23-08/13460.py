import sys
read = sys.stdin.readline

N, M = map(int, read().split())
graph = []
rx, ry, bx, by = 0
for _ in range(N):
    line = list(read().strip())
    if 'R' in line:
        rx, ry = line.index('R'), _
    if 'B' in line:
        bx, by = line.index('B'), _
    graph.append(line)
