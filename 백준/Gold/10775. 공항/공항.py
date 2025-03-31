import sys
input = sys.stdin.readline

def solution(G, P, g):
    answer = 0
    parent = [i for i in range(G + 1)]

    def find(a):
        if a != parent[a]:
            parent[a] = find(parent[a])
        return parent[a]

    for i in range(P):
        now = find(g[i])
        if now == 0:
            break
        parent[now] = find(now - 1)
        answer += 1

    return answer

G = int(input())
P = int(input())
g = [int(input()) for _ in range(P)]
print(solution(G, P, g))
