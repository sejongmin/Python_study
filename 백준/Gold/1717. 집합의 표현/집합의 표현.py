import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def solution(n, m, orders):
    parent = [i for i in range(n + 1)]
    def find(e):
        if parent[e] != e:
            parent[e] = find(parent[e])
        return parent[e]
    
    def union(a, b):
        a = find(a)
        b = find(b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    for o, a, b in orders:
        if o == 0:
            union(a, b)
        elif o == 1:
            if find(a) == find(b):
                print("YES")
            else:
                print("NO")

n, m = map(int, input().split())
orders = [list(map(int, input().split())) for _ in range(m)]
solution(n, m, orders)
