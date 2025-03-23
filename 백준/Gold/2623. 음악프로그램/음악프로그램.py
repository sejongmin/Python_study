import sys
from collections import deque
input = sys.stdin.readline

def solution(N, M, arr):
    answer = []
    indegree = [0] * (N + 1)
    graph = {i: [] for i in range(1, N + 1)}

    for i in range(M):
        for j in range(1, arr[i][0]):
            graph[arr[i][j]].append(arr[i][j + 1])
            indegree[arr[i][j + 1]] += 1

    q = deque()
    for i in range(1, N + 1):
        if indegree[i] == 0:
            answer.append(i)
            q.append(i)

    while q:
        now = q.popleft()
        for next in graph[now]:
            indegree[next] -= 1
            if indegree[next] == 0:
                answer.append(next)
                q.append(next)

    if N == len(answer):
        print(*answer, sep="\n")
    else:
        print(0)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
solution(N, M, arr)
