import sys
import heapq
input = sys.stdin.readline

def solution(N, M, problems):
    answer = []
    graph = {i: [] for i in range(1, N + 1)}
    indegree = [0] * (N + 1)
    
    for i in range(M):
        indegree[problems[i][1]] += 1
        graph[problems[i][0]].append(problems[i][1])

    q = []
    for i in range(1, N + 1):
        if indegree[i] == 0:
            heapq.heappush(q, i)

    while q:
        now = heapq.heappop(q)
        answer.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                heapq.heappush(q, i)

    print(*answer)

N, M = map(int, input().split())
problems = [list(map(int, input().split())) for _ in range(M)]
solution(N, M, problems)
