import sys
from collections import deque
input = sys.stdin.readline

def solution(N, M, arr):
    answer = []
    graph = {i: [] for i in range(1, N + 1)}
    indegree = [0] * (N + 1)
    for i in range(M):
        indegree[arr[i][1]] += 1
        graph[arr[i][0]].append(arr[i][1])

    q = deque()
    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        answer.append(now)
        for next in graph[now]:
            indegree[next] -= 1
            if indegree[next] == 0:
                q.append(next)

    print(*answer)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
solution(N, M, arr)
