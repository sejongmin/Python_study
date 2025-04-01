import sys
input = sys.stdin.readline

def solution(N: int, arr: list) -> int:
    sub = [arr[0]]

    for i in range(1, N):
        if sub[-1] < arr[i]:
            sub.append(arr[i])
        elif sub[-1] > arr[i]:
            left, right = 0, len(sub) - 1
            while left < right:
                mid = (left + right) // 2
                if arr[i] > sub[mid]:
                    left = mid + 1
                else:
                    right = mid
            sub[left] = arr[i]
    return len(sub)

N = int(input())
arr = list(map(int, input().split()))
print(solution(N, arr))
