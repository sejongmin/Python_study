import sys
input = sys.stdin.readline

def solution(N, M, edges):
    parents = [i for i in range(N + 1)]
    edges.sort(key=lambda x: -x[2])
    
    def find(a):
        if a != parents[a]:
            parents[a] = find(parents[a])
        return parents[a]
    
    def union(a, b):
        a = find(a)
        b = find(b)
        if a > b:
            parents[a] = b
        else:
            parents[b] = a
    
    answer = 0
    cnt = 0
    while edges:
        if cnt == N - 1:
            break
        a, b, c = edges.pop()
        if find(a) == find(b):
            continue
        union(a, b)
        answer += c
        cnt += 1
    print(answer)

N = int(input())
M = int(input())
edges = [list(map(int, input().split())) for _ in range(M)]
solution(N, M, edges)