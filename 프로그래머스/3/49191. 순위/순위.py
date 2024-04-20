def solution(n, results):
    answer = 0
    graph = {i:[set(), set()] for i in range(1, n + 1)}
    for win, lose in results:
        graph[win][1].add(lose)
        graph[lose][0].add(win)
        
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i in graph[j][0]:
                graph[j][0] = graph[j][0].union(graph[i][0])
            if i in graph[j][1]:
                graph[j][1] = graph[j][1].union(graph[i][1])
                
    for i in range(1, n + 1):
        if len(graph[i][0]) + len(graph[i][1]) == n - 1:
            answer += 1
    return answer