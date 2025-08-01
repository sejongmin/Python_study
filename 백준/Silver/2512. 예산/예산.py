import sys
input = sys.stdin.readline

def solution(N: int, requests: list, M: int) -> int:
    if sum(requests) <= M:
        return max(requests)

    result = 0
    left, right = 0, int(1e9)
    while left <= right:
        mid = (left + right) // 2
        now = 0
        for request in requests:
            if request < mid:
                now += request
            else:
                now += mid
        if now <= M:
            result = mid
            left = mid + 1
        elif now > M:
            right = mid - 1

    return result

if __name__ == "__main__":
    N = int(input())
    requests = list(map(int, input().split()))
    M = int(input())
    print(solution(N, requests, M))

