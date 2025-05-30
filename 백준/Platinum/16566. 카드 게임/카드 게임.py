import sys
from bisect import bisect_right
input = sys.stdin.readline

def solution(N, M, K, cards, arr):
    answer = []
    visited = [False] * M
    parents = [i for i in range(M + 1)]

    def find(a):
        if a != parents[a]:
            parents[a] = find(parents[a])
        return parents[a]

    def union(a, b):
        a = find(a)
        b = find(b)
        if a < b:
            a, b = b, a
        parents[b] = a

    cards.sort()
    for i in range(K):
        idx = bisect_right(cards, arr[i])
        idx = find(idx)
        answer.append(cards[idx])
        visited[idx] = True
        union(idx, idx + 1)
    print(*answer, sep='\n')

N, M, K = map(int, input().split())
cards = list(map(int, input().split()))
arr = list(map(int, input().split()))
solution(N, M, K, cards, arr)