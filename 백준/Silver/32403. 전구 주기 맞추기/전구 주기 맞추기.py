import sys
input = sys.stdin.readline

def solution(N, T, arr):
    answer = 0
    nums = [1, T]
    for i in range(2, int(T ** 1//2)):
        if T % i == 0:
            nums.append(i)
            nums.append(T // i)
    nums.sort()

    for a in arr:
        if a >= T:
            answer += a - T
            continue
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right + 1) // 2
            if a > nums[mid]:
                left = mid
            elif a < nums[mid]:
                right = mid - 1
            else:
                left = mid
                break
        right = left + 1
        answer += min(a - nums[left], nums[right] - a)
    
    print(answer)
    return

N, T = map(int, input().split())
arr = list(map(int, input().split()))
solution(N, T, arr)