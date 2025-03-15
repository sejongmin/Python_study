import sys
input = sys.stdin.readline

def solution(n, m, arr):
    parent = [i for i in range(n)]

    def find(a):
        while a != parent[a]:
            a = parent[a]
        return a
    
    def union(a, b):
        a = find(a)
        b = find(b)
        if a < b:
            parent[b] = a
        elif a > b:
            parent[a] = b

    for i in range(m):
        if find(arr[i][0]) != find(arr[i][1]):
            union(arr[i][0], arr[i][1])
        else:
            return i + 1

    return 0

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
print(solution(n, m, arr))
