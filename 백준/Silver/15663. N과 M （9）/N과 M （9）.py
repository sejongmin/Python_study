import sys
input = sys.stdin.readline

def solution(N, M, series):
    answer = []
    series.sort()
    def back(arr, depth, dup):
        nonlocal N, M, series
        if depth == M:
            answer.append(arr[:])
            return
        for i in range(N):
            if i not in dup:
                arr.append(series[i])
                dup.add(i)
                back(arr, depth + 1, dup)
                dup.remove(i)
                arr.pop()
    back([], 0, set())
    answer = sorted(list(set(map(tuple, answer))))
    for i in range(len(answer)):
        print(*answer[i], sep=' ')
N, M = map(int, input().split())
series = list(map(int, input().split()))
solution(N, M, series)