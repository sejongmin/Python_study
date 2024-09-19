import sys
input = sys.stdin.readline

def solution(N, A):
    arr = [A[0]]
    for i in range(1, N):
        if arr[-1] < A[i]:
            arr.append(A[i])
        else:
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] < A[i]:
                    left = mid + 1
                else:
                    right = mid - 1
            arr[left] = A[i]
    return len(arr)

N = int(input())
A = list(map(int, input().split()))
print(solution(N, A))