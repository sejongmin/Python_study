import sys
from collections import deque
input = sys.stdin.readline

def solution(N, populations, graph):
    answer = 1000
    total = sum(populations)
    nodes = [i for i in range(1, N + 1)]

    def is_connected(group, graph):
        visited = set()
        q = deque([group[0]])
        visited.add(group[0])

        while q:
            now = q.popleft()
            for node in graph[now]:
                if node in group and node not in visited:
                    visited.add(node)
                    q.append(node)
        
        return len(group) == len(visited)

    for i in range(1, (1 << N) - 1):
        group_a = []
        for j in range(N):
            if i & (1 << j):
                group_a.append(nodes[j])
        group_b = [x for x in nodes if x not in group_a]

        if is_connected(group_a, graph) and is_connected(group_b, graph):
            sum_a = sum(populations[i - 1] for i in group_a)
            answer = min(answer, abs(total - 2 * sum_a))
    
    print(answer if answer != 1000 else -1)

N = int(input())
populations = list(map(int, input().split()))
graph = {}
for i in range(1, N + 1):
    arr = list(map(int, input().split()))
    graph[i] = arr[1:]
solution(N, populations, graph)
