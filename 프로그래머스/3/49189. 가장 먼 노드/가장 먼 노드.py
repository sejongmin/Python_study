def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    
    for i, j in edge:
        graph[i].append(j)
        graph[j].append(i)
    
    arr = [0] * (n + 1)
    visit = [False] * (n + 1)
    q = [1]
    visit[1] = True
    
    while q:
        now = q.pop(0)
        for node in graph[now]:
            if not visit[node]:
                q.append(node)
                arr[node] = arr[now] + 1
                visit[node] = True
    
    m = max(arr)
    answer = arr.count(m)
    return answer