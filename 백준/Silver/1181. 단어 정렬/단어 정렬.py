import sys
input = sys.stdin.readline

N = int(input())
graph = []
len_ = []
for i in range(N):
    graph.append(input().strip())
    len_.append(len(graph[i]))

graph = list(set(graph))
len_ = list(set(len_))

graph.sort()
len_.sort()

for i in len_:
    for j in graph:
        if i == len(j):
            print(j)
