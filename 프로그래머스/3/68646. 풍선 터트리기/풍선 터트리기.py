def solution(a):
    answer = 2 if len(a) > 1 else 1
    idx = a.index(min(a))
    min_value = a[0]
    for i in range(1, idx):
        if min_value > a[i]:
            answer += 1
            min_value = a[i]
    min_value = a[-1]
    for i in range(len(a) - 2, idx - 1, -1):
        if min_value > a[i]:
            answer += 1
            min_value = a[i]
            
    return answer