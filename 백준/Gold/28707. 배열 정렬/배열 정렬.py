import sys
import heapq
input = sys.stdin.readline

def solution(N, arr, M, controls):
    INF = int(1e9)
    now = tuple(arr)
    ans = tuple(sorted(arr))

    q = []
    visited = {}
    heapq.heappush(q, (0, now))
    visited[now] = 0
    while q:
        cost, now = heapq.heappop(q)
        if ans == now:
            return cost
        if cost > visited[now]:
            continue
        for l, r, c in controls:
            l -= 1
            r -= 1
            new = tuple(now[i] if i != l and i != r else (now[r] if i == l else now[l]) for i in range(N))
            if visited.get(new, INF) <= cost + c:
                continue
            visited[new] = cost + c
            heapq.heappush(q, (cost + c, new))
    return -1

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
controls = [list(map(int, input().split())) for _ in range(M)]
print(solution(N, arr, M, controls))
