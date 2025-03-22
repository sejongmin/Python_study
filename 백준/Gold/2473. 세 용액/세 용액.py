import sys
input = sys.stdin.readline

def solution(N, arr):
    arr.sort()
    answer = []
    min_val = int(3*10e9)

    for i in range(N - 2):
        left = i + 1
        right = N - 1

        while left < right:
            value = arr[i] + arr[left] + arr[right]

            if min_val > abs(value):
                min_val = abs(value)
                answer = [arr[i], arr[left], arr[right]]

            if value > 0:
                right -= 1
            elif value < 0:
                left += 1
            elif value == 0:
                print(arr[i], arr[left], arr[right])
                return

    print(*answer)
    return

N = int(input())
arr = list(map(int, input().split()))
solution(N, arr)
