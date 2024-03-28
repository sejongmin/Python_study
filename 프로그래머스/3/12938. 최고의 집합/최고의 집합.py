def solution(n, s):
    if n > s:
        return [-1]
    answer = [s // n for _ in range(n)]
    if s % n == 0:
        return answer
    for i in range(s % n):
        answer[n - i - 1] += 1
    return answer
    
    