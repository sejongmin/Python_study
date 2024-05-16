def solution(n, costs):
    answer = 0
    parent = [i for i in range(n)]
    costs.sort(key=lambda x:x[2])
    
    def find(parent, a):
        if a != parent[a]:
            parent[a] = find(parent, parent[a])
        return parent[a]
    
    def union(a, b):
        nonlocal parent
        pa = find(parent, a)
        pb = find(parent, b)
        if pa < pb:
            parent[pb] = pa
        elif pa > pb:
            parent[pa] = pb

    for cost in costs:
        if find(parent, cost[0]) != find(parent, cost[1]):
            union(cost[0], cost[1])
            answer += cost[2]
    
    return answer