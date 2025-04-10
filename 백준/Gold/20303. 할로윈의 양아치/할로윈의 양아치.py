import sys
input = sys.stdin.readline

def solution(N, M, K, c, r):
    friends = [i for i in range(N + 1)]
    candy = {}

    def find(a):
        if a != friends[a]:
            friends[a] = find(friends[a])
        return friends[a]
    
    def union(a, b):
        fa = find(a)
        fb = find(b)
        if fa > fb:
            friends[fa] = fb
        elif fa < fb:
            friends[fb] = fa

    for i in range(M):
        a, b = r[i]
        union(a, b)
    
    for i in range(1, N + 1):
        root = find(i)
        candy[root] = candy.get(root, [0, 0])
        candy[root][0] += c[i - 1]
        candy[root][1] += 1
    
    dp = [0] * K
    for val, size in candy.values():
        for j in range(K - 1, size - 1, -1):
            dp[j] = max(dp[j], dp[j - size] + val)

    return dp[-1]

N, M, K = map(int, input().split())
c = list(map(int, input().split()))
r = [list(map(int, input().split())) for _ in range(M)]
print(solution(N, M, K, c, r))
