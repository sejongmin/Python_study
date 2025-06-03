import sys
input = sys.stdin.readline

def solution(N, lines):
    group = [i for i in range(N)]

    def find(a):
        if a != group[a]:
            group[a] = find(group[a])
        return group[a]
    
    def union(a, b):
        a = find(a)
        b = find(b)

        if a > b:
            group[a] = b
        elif a < b:
            group[b] = a
    
    def cross(line1, line2):
        a = (line1[0], line1[1])
        b = (line1[2], line1[3])
        c = (line2[0], line2[1])
        d = (line2[2], line2[3])

        if a > b:
            a, b = b, a
        if c > d:
            c, d = d, c

        t1 = (a[0] * b[1] + b[0] * c[1] + c[0] * a[1]) - (a[1] * b[0] + b[1] * c[0] + c[1] * a[0])
        t2 = (a[0] * b[1] + b[0] * d[1] + d[0] * a[1]) - (a[1] * b[0] + b[1] * d[0] + d[1] * a[0])

        if t1 * t2 <= 0:
            if t1 == 0 and t2 == 0:
                return b > c and a < d
            return True
        return False

    for i in range(N - 1):
        for j in range(i + 1, N):
            if cross(lines[i], lines[j]) and cross(lines[j], lines[i]):
                union(i, j)

    roots = set(find(i) for i in range(N))
    print(len(roots))
    count = {}
    for i in range(N):
        root = find(i)
        count[root] = count.get(root, 0) + 1
    print(max(count.values()))


N = int(input())
lines = [tuple(map(int, input().split())) for _ in range(N)]
solution(N, lines)
