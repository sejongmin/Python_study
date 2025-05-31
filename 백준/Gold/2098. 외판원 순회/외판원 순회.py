import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline
INF = int(1e9)

def solution(N, graph):
    dp = {}
    
    def dfs(now, visited):
        if visited == (1 << N) - 1:
            return graph[now][0] if graph[now][0] else INF
        
        if (now, visited) in dp:
            return dp[(now, visited)]

        for i in range(1, N):
            if not graph[now][i]:
                continue
            if visited & (1 << i):
                continue
            dp[(now, visited)] = min(dp.get((now, visited), INF), dfs(i, visited | (1 << i)) + graph[now][i])
        return dp.get((now, visited), INF)
    print(dfs(0, 1))

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
solution(N, graph)
