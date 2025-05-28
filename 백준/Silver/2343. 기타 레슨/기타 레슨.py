import sys
input = sys.stdin.readline

def solution(N, M, lectures):
    answer = 0
    left = 0
    right = 0
    for lecture in lectures:
        if left < lecture:
            left = lecture
        right += lecture

    while left <= right:
        mid = (left + right) // 2
        total = 0
        count = 1
        for lecture in lectures:
            if total + lecture > mid:
                count += 1
                total = 0
            total += lecture
        
        if count <= M:
            answer = mid
            right = mid - 1
        elif count > M:
            left = mid + 1
    
    return answer

N, M = map(int, input().split())
lectures = list(map(int, input().split()))
print(solution(N, M, lectures))
