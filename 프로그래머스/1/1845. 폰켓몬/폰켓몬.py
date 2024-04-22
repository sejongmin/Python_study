def solution(nums):
    N = len(nums)
    set_nums = set(nums)
    return min(N // 2, len(set_nums))
    