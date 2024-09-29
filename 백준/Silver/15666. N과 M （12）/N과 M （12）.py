import sys
input = sys.stdin.readline

def solution(N, M, series):
    series = sorted(list(set(series)))
    def back(arr, depth, index):
        nonlocal M, series
        if depth == M:
            print(*arr)
            return
        for i in range(index, len(series)):
            arr.append(series[i])
            back(arr, depth + 1, i)
            arr.pop()
    back([], 0, 0)

N, M = map(int, input().split())
series = list(map(int, input().split()))
solution(N, M, series)