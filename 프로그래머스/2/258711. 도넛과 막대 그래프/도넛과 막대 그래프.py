def solution(edges):
    answer = [0, 0, 0, 0]
    out_edges = {}
    in_edges = {}
    
    for edge in edges:
        out_edges[edge[0]] = out_edges.get(edge[0], 0) + 1
        in_edges[edge[0]] = in_edges.get(edge[0], 0)
        in_edges[edge[1]] = in_edges.get(edge[1], 0) + 1
        out_edges[edge[1]] = out_edges.get(edge[1], 0)
    
    for i in out_edges.keys():
        if out_edges[i] > 1 and in_edges[i] == 0:
            answer[0] = i
        if out_edges[i] == 0 and in_edges[i] >= 1:
            answer[2] += 1
        if out_edges[i] == 2 and in_edges[i] >= 2:
            answer[3] += 1
    answer[1] = out_edges[answer[0]] - answer[2] - answer[3]

    return answer