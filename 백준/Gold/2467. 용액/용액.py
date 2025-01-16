import sys
input = sys.stdin.readline

def solution(N: int, arr: list) -> None:
    answer = [int(10e9), -1, -1]

    left = 0
    right = N - 1
    while left < right:
        now = arr[left] + arr[right]
        if answer[0] > abs(now):
            answer[0] = abs(now)
            answer[1] = left
            answer[2] = right
        if now > 0:
            right -= 1
        elif now < 0:
            left += 1
        else:
            break
    
    print(arr[answer[1]], arr[answer[2]])
        
N = int(input())
arr = list(map(int, input().split()))
solution(N, arr)
