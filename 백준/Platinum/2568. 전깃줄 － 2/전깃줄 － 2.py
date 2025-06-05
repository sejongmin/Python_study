import sys
from bisect import bisect_left
input = sys.stdin.readline

def solution(N, edges):
    answer = []
    possible = set()
    edges.sort(key=lambda x: x[1])
    arr = [edges[0][0]]
    dp = [(0, edges[0][0])]
    cnt = 0

    for a, _ in edges:
        if arr[-1] < a:
            cnt += 1
            arr.append(a)
            dp.append((cnt, a))
        elif arr[-1] > a:
            idx = bisect_left(arr, a)
            arr[idx] = a
            dp.append((idx, a))
    print(N - cnt - 1)

    for i in range(len(dp) - 1, -1, -1):
        if dp[i][0] == cnt:
            possible.add(dp[i][1])
            cnt -= 1

    for a, _ in edges:
        if a not in possible:
            answer.append(a)
    print(*sorted(answer), sep='\n')

N = int(input())
edges = [list(map(int, input().split())) for _ in range(N)]
solution(N, edges)
