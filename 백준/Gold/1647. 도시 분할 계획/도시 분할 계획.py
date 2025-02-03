import sys
input = sys.stdin.readline

def solution(N: int, M: int, roads: list) -> int:
    answer = 0
    parents = [i for i in range(N + 1)]
    
    def find(a):
        if a == parents[a]:
            return a
        return find(parents[a])
    
    def union(a, b):
        a = find(a)
        b = find(b)

        if a > b:
            parents[b] = a
        else:
            parents[a] = b

    roads.sort(key=lambda x: x[2])

    last = 0
    for road in roads:
        a, b, c = road
        if find(a) != find(b):
            union(a, b)
            answer += c
            last = c
    
    return answer - last

N, M = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(M)]
print(solution(N, M, roads))
