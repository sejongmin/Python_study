import sys
input = sys.stdin.readline

def solution(N: int, arr: list):
    length = 1
    dp = [1]
    sub = [arr[0]]

    for i in range(1, N):
        if sub[-1] < arr[i]:
            sub.append(arr[i])
            length = length + 1
            dp.append(length)
            continue
        elif sub[-1] >= arr[i]:
            left, right = 0, len(sub) - 1
            while left < right:
                mid = (left + right) // 2
                if arr[i] > sub[mid]:
                    left = mid + 1
                else:
                    right = mid
            sub[left] = arr[i]
            dp.append(left + 1)
    print(length)

    answer = []
    for i in range(N - 1, -1, -1):
        if length == dp[i]:
            answer.append(arr[i])
            length = length - 1
    answer.reverse()
    print(*answer)

N = int(input())
arr = list(map(int, input().split()))
solution(N, arr)
